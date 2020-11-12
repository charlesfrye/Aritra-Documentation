# Builtin
import ast
import tokenize

# Extract and Parse
from Parser import parse, extract

def parse_file(filename):
    '''
    Generates the node in the AST

    Arguments: filename <demo.py>

    Return: node of AST
    '''
    with tokenize.open(filename) as f:
        return ast.parse(f.read(), filename=filename, mode='exec')

def compute_interval(node):
    min_lineno = node.lineno
    max_lineno = node.lineno
    for node in ast.walk(node):
        if hasattr(node, "lineno"):
            min_lineno = min(min_lineno, node.lineno)
            max_lineno = max(max_lineno, node.lineno)
    return (min_lineno, max_lineno + 1)

# Take the root node
root = parse_file("demo.py")
info_name_line = []

for node in ast.iter_child_nodes(root):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
        has_doc = False
        # first_level.append(node)
        if ast.get_docstring(node):
            has_doc = True
        name = node.name
        line = compute_interval(node)
        children = []
        # info_name_line.append({"name":node.name, "line":compute_interval(node)})
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.ClassDef)):
                if ast.get_docstring(child):
                    name_child = '{}.{}'.format(node.name, child.name)
                    name_line = compute_interval(child)
                    child_dict = {"name":name_child, "line":name_line}
                    children.append(child_dict)
                    # info_name_line.append({"name":name_var, "line":compute_interval(child)})
        parent_dict = {"name":name, "line": line, "has_doc": has_doc, "children": children}
        info_name_line.append(parent_dict)

markdown = ''
md_source = open('template.txt').read()

for element in info_name_line:
    if element['has_doc']:
        # Has docstring
        h1 = element['name']
        line = element['line']
        query = element['name']
        doc_dict = extract.extract(filestr='demo.py',query=query)
        c_m = ''
        if doc_dict['class'] != '':
            c_m = 'class'
        else:
            c_m = 'def'
        sig = doc_dict['signature']
        google_doc = parse.GoogleDocString(doc_dict['docstring'])
        parsed_list = google_doc.parse(mark_code_blocks=True)
        summary = parsed_list[0]['text']
        table_arg = ''
        table_att = ''
        hint = ''
        returns=''
        example = ''
        for item in parsed_list:
            if item["header"] == "Args":
                table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                for arg in item["args"]:
                    table_arg += """|{}|{}|{}|\n""".format(
                        arg['field'],
                        arg['signature'],
                        extract.format_txt(arg['description'])
                    )
                
            if item["header"] == "Attributes":
                table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                for arg in item["args"]:
                    table_att += """|{}|{}|{}|\n""".format(
                        arg['field'],
                        arg['signature'],
                        extract.format_txt(arg['description'])
                    )

            if item["header"] == "Raises":
                for arg in  item['args']:
                    hint='{% hint style="info" %}\n'
                    hint += arg['signature']+':'+arg['description']+'\n'
                    hint += '{% endhint %}'
            if item["header"] == "Examples":
                example='**Example**\n\n'
                example += item['text']
            if item["header"] == "Returns":
                returns = '**Reutrns**\n\n'
                returns += item['text']
        
        temp = md_source.format(
            "# {}".format(h1), #header
            line[0], #line begin
            line[1], #line end
            '`{} {}{}`'.format(c_m, h1, sig), #signature
            summary, #summary
            table_arg, # arguments
            table_att, # attributes
            hint, #hint
            returns, #returns
            example #example
        )
        markdown += temp
        # Check for children
        if element['children']:
            for child in element['children']:
                h2 = child['name']
                line = child['line']
                query = child['name']
                doc_dict = extract.extract(filestr='demo.py',query=query)
                c_m = ''
                if doc_dict['class'] != '':
                    c_m = 'class'
                else:
                    c_m = 'def'
                sig = doc_dict['signature']
                google_doc = parse.GoogleDocString(doc_dict['docstring'])
                parsed_list = google_doc.parse(mark_code_blocks=True)
                summary = parsed_list[0]['text']
                table_arg = ''
                table_att = ''
                hint = ''
                returns=''
                example = ''
                for item in parsed_list:
                    if item["header"] == "Args":
                        table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                        for arg in item["args"]:
                            table_arg += """|{}|{}|{}|\n""".format(
                                arg['field'],
                                arg['signature'],
                                extract.format_txt(arg['description'])
                            )
                        
                    if item["header"] == "Attributes":
                        table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                        for arg in item["args"]:
                            table_att += """|{}|{}|{}|\n""".format(
                                arg['field'],
                                arg['signature'],
                                extract.format_txt(arg['description'])
                            )

                    if item["header"] == "Raises":
                        for arg in  item['args']:
                            hint='{% hint style="info" %}\n'
                            hint += arg['signature']+':'+arg['description']+'\n'
                            hint += '{% endhint %}'
                    if item["header"] == "Examples":
                        example='**Example**\n\n'
                        example += item['text']
                    if item["header"] == "Returns":
                        returns = '**Reutrns**\n\n'
                        returns += item['text']
                
                temp = md_source.format(
                    "## {}".format(h2), #header
                    line[0], #line begin
                    line[1], #line end
                    '`{} {}{}`'.format(c_m, h2, sig), #signature
                    summary, #summary
                    table_arg, # arguments
                    table_att, # attributes
                    hint, #hint
                    returns, #returns
                    example #example
                )
                markdown += temp

        
    elif element['children']:
        h1 = element['name']
        line = element['line']

        temp = md_source.format(
            "# {}".format(h1), #heading
            line[0], #line begin
            line[1], #line end
            '', 
            '',
            '',
            '',
            '',
            '',
            ''
        )
        markdown += temp

        # Get into children
        for child in element['children']:
            h2 = child['name']
            line = child['line']
            query = child['name']
            doc_dict = extract.extract(filestr='demo.py',query=query)
            c_m = ''
            if doc_dict['class'] != '':
                c_m = 'class'
            else:
                c_m = 'def'
            sig = doc_dict['signature']
            google_doc = parse.GoogleDocString(doc_dict['docstring'])
            parsed_list = google_doc.parse(mark_code_blocks=True)
            summary = parsed_list[0]['text']
            table_arg = ''
            table_att = ''
            hint = ''
            returns=''
            example = ''
            for item in parsed_list:
                if item["header"] == "Args":
                    table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                    for arg in item["args"]:
                        table_arg += """|{}|{}|{}|\n""".format(
                            arg['field'],
                            arg['signature'],
                            extract.format_txt(arg['description'])
                        )
                    
                if item["header"] == "Attributes":
                    table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                    for arg in item["args"]:
                        table_att += """|{}|{}|{}|\n""".format(
                            arg['field'],
                            arg['signature'],
                            extract.format_txt(arg['description'])
                        )

                if item["header"] == "Raises":
                    for arg in  item['args']:
                        hint='{% hint style="info" %}\n'
                        hint += arg['signature']+':'+arg['description']+'\n'
                        hint += '{% endhint %}'
                if item["header"] == "Examples":
                    example='**Example**\n\n'
                    example += item['text']
                if item["header"] == "Returns":
                    returns = '**Reutrns**\n\n'
                    returns += item['text']
            
            temp = md_source.format(
                "## {}".format(h2), #header
                line[0], #line begin
                line[1], #line end
                '`{} {}{}`'.format(c_m, h2, sig), #signature
                summary, #summary
                table_arg, # arguments
                table_att, # attributes
                hint, #hint
                returns, #returns
                example #example
            )
            markdown += temp


with open('doc.md', 'w') as f:
    f.write(markdown)