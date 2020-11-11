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
        h1 = element['name']
        line = element['line']

        query = element['name']
        doc_dict = extract.extract(filestr='demo.py',query=query)
        sig = doc_dict['signature']
        google_doc = parse.GoogleDocString(doc_dict['docstring'])
        parsed_list = google_doc.parse(mark_code_blocks=True)
        summary = parsed_list[0]['text']
        for item in parsed_list:
            if item["header"] == "Arguments":
                # Need args
                pass
            if item["header"] == "Attributes":
                # Need attributes
                pass
            if item["header"] == "Raises":
                # Need hints
                pass
            if item["header"] == "Examples":
                # Need examples
                pass
        
        temp = md_source.format(
            "# {}".format(h1),
            line[0],
            line[1],
            '`{}`'.format(sig),
            summary,
            '',
            '',
            '',
            '',
            ''
        )
        markdown += temp
        # Check for children
        if element['children']:
            pass

        
    elif element['children']:
        h1 = element['name']
        line = element['line']

        temp = md_source.format(
            "# {}".format(h1),
            line[0],
            line[1],
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


with open('doc.md', 'w') as f:
    f.write(markdown)