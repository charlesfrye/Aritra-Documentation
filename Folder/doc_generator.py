# Builtin
import ast
import tokenize

# Files
from parser import parse_docstring, compute_interval

md_source = open('template.txt').read()

md_export = ''

def parse_file(filename):
    '''
    Generates the node in the AST

    Arguments: filename <demo.py>

    Return: node of AST
    '''
    with tokenize.open(filename) as f:
        return ast.parse(f.read(), filename=filename)


for item in ast.walk(parse_file("demo.py")):
    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        # print('Name: {}'.format(item.name))
        # print('Line Numbers: {}'.format(compute_interval(item)))
        # print('Docstring: {}'.format(ast.get_docstring(item)))

        name = item.name
        begin, end = compute_interval(item)
        docstring = ast.get_docstring(item)

        parsed_doc = parse_docstring(docstring)

        # For the table:
        s = ''
        for element in parsed_doc['params']:
            st = '|'.join([element["name"],str(element["type"]),str(element["doc"])])
            st = '|{}|'.format(st)
            s += '{}\n'.format(st)

        markdown = md_source.format(
            name,
            begin,
            end-1,
            parsed_doc['short_description'],
            parsed_doc['long_description'],
            s,
            parsed_doc['returns'],
        )
        md_export += markdown

with open('doc.md', 'w') as f:
    f.write(md_export)