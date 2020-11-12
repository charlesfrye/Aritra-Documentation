# USAGE $python doc_gen.py CODE/code.py DOCS/docs.md
import ast
import _ast
import sys
import tokenize

from mydocstring.extract import extract, format_txt
from mydocstring import parse

TEMPLATE_FILE = open('template.txt').read()
SOURCE_CODE = sys.argv[1]
MARKDOWN_FILE = sys.argv[2]

def compute_interval(node):
    min_lineno = node.lineno
    max_lineno = node.lineno
    for node in ast.walk(node):
        if hasattr(node, "lineno"):
            min_lineno = min(min_lineno, node.lineno)
            max_lineno = max(max_lineno, node.lineno)
    return (min_lineno, max_lineno)

def has_doc(node):
    if ast.get_docstring(node):
        return True
    else:
        return False

def inspect_module(module_path):
    """Used to fetch the names of classes and fuctions.

    Arguments:
        module_path (str): Complete path of the module
    
    Returns:
        tuple: A tuple of `(module_classes, module_functions)`
    
    Example:
        ```
        module_classes, module_functions = inspect_module(module_path)
        ```
    """
    with tokenize.open(module_path) as mf:
        tree = ast.parse(mf.read())
    module_classes = []
    module_functions = []
    for item in tree.body:
        if isinstance(item, _ast.ClassDef):
            # IF CLASS
            module_methods = []
            for nest_item in item.body:
                if isinstance(nest_item, _ast.FunctionDef):
                    # IF METHOD
                    if has_doc(nest_item):
                        module_methods.append((nest_item.name, compute_interval(nest_item)))
            if len(module_methods) != 0 or has_doc(item):
                module_classes.append(((item.name, compute_interval(item), has_doc(item)),module_methods))

        elif isinstance(item, _ast.FunctionDef):
            # ELSE IF FUNCTION
            if has_doc(item):
                module_functions.append((item.name, compute_interval(item)))

    return (module_classes, module_functions)

def setup_google(query, signature=None, config=None):
    extracted = extract(SOURCE_CODE, query)
    # print(extracted)
    google = parse.GoogleDocString(
        extracted['docstring'].lstrip('\n'),
        signature=signature,
        config=config)
    return extracted, google

def create_md(query, line, header, has_doc=True, signature=None, config=None):
    if has_doc:
        extracted, google = setup_google(
            query=query,
            signature=signature,
            config=config)
        docstr = google.parse()
        # print(query)
        # print(docstr)
        table_arg = ''
        table_att = ''
        hint = ''
        example = ''
        returns = ''
        for item in docstr:
            # CHECK FOR ARGUMENTS
            if item["header"] == "Arguments":
                table_arg = """| **Arguments** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                for arg in item["args"]:
                    table_arg += """|{}|{}|{}|\n""".format(
                        arg['field'],
                        arg['signature'],
                        format_txt(arg['description'])
                    )
            
            # CHECK FOR ATTRIBUTES
            if item["header"] == "Attributes":
                table_att = """| **Attributes** | **Datatype** | **Description** |\n|:--:|:--:|:--|\n"""
                for arg in item["args"]:
                    table_att += """|{}|{}|{}|\n""".format(
                        arg['field'],
                        arg['signature'],
                        format_txt(arg['description'])
                    )
            
            # CHECK FOR RAISES
            if item["header"] == "Raises":
                for arg in  item['args']:
                    hint='{% hint style="info" %}\n'
                    hint += arg['signature']+':'+arg['description']+'\n'
                    hint += '{% endhint %}'
            
            # CHECK FOR EXAMPLES
            if item["header"] == "Examples":
                example='**Example**\n\n'
                example += item['text']
            
            # CHECK FOR RETURNS
            if item["header"] == "Returns":
                returns = '**Reutrns**\n\n'
                returns += item['text']
        
        if extracted['source'] == '':
            sig = '`{}`'.format(query)
        else:
            sig = '`{}`'.format(extracted['source'].split('\n')[0])

        return TEMPLATE_FILE.format(
                header, #header
                SOURCE_CODE, #source file in repo: https://github.com/ariG23498/Aritra-Documentation/blob/master/____
                line[0], #line begin
                line[1], #line end
                sig, #function signature: extract['source']
                docstr[0]['text'].lstrip('\n'), #summary
                table_arg, #table_args 
                table_att, #table_att
                hint, #hint
                returns, #returns
                example #example
            )
    else:
        return TEMPLATE_FILE.format(
            header, #header
            SOURCE_CODE, #source file in repo: https://github.com/ariG23498/Aritra-Documentation/blob/master/____
            line[0], #line begin
            line[1], #line end
            '', #function signature: extract['source']
            '', #summary: parse[0]['text']
            '', #table_args 
            '', #table_att
            '', #hint
            '', #returns
            '' #example
        )


module_classes, module_functions = inspect_module(SOURCE_CODE)
markdown = ''
# print('**MODULE CLASSES with METHODS**')
for class_item, method_items in module_classes:
    class_name = class_item[0]
    class_line = class_item[1]
    class_has_doc = class_item[2]
    header = "# {}".format(class_name)
    md = create_md(class_name, class_line, header, class_has_doc)
    markdown += '{}\n'.format(md)
    # print("{} {} {}".format(class_name, class_line, class_has_doc))
    for method_item in method_items:
        method_name = method_item[0]
        method_line = method_item[1]
        header = "## {}".format(method_name)
        md = create_md('{}.{}'.format(class_name,method_name), method_line, header)
        markdown += '{}\n'.format(md)
        # print('  {} {}'.format(method_name, method_line))
      
# print('**MODULE FUNCTIONS**')
for func_item in module_functions:
    func_name = func_item[0]
    func_line = func_item[1]
    header = "# {}".format(func_name)
    md = create_md(func_name, func_line, header)
    markdown += '{}\n'.format(md)
    # print("{} {}".format(func_name, func_line))

with open(MARKDOWN_FILE, 'w') as f:
    f.write(markdown)