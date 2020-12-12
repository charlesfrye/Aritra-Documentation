from docparse import *
import ast
import _ast
import tokenize

def compute_interval(node):
    """Computes the beginning and the ending line number"""
    min_lineno = node.lineno
    max_lineno = node.lineno
    for node in ast.walk(node):
        if hasattr(node, "lineno"):
            min_lineno = min(min_lineno, node.lineno)
            max_lineno = max(max_lineno, node.lineno)
    return (min_lineno, max_lineno)

def has_doc(node):
    """Checks for docstring"""
    if ast.get_docstring(node):
        return True
    else:
        return False

def inspect_module(module_path):
    """Inspects the whole module"""
    with tokenize.open(module_path) as mf:
        tree = ast.parse(mf.read())
    module_details = []
    if has_doc(tree):
        # IF MODULE
        module_details.append({
            'name':'.',
            'lineno':(0,0),
            'hasdoc':True,})
    for item in tree.body:
        if isinstance(item, _ast.ClassDef):
            # IF CLASS
            module_methods = []
            for nest_item in item.body:
                if isinstance(nest_item, _ast.FunctionDef):
                    # IF METHOD
                    if has_doc(nest_item):
                        module_methods.append({
                            'name':'{}.{}'.format(item.name,nest_item.name),
                            'lineno':compute_interval(nest_item),
                            'hasdoc':True,
                            'source':ast.get_source_segment(module_path,nest_item)})
            if len(module_methods) != 0 or has_doc(item):
                module_details.append((item.name, compute_interval(item), has_doc(item)))
                for i in module_methods:
                    module_details.append(i)
        elif isinstance(item, _ast.FunctionDef):
            # ELSE IF FUNCTION
            if has_doc(item):
                module_details.append((item.name, compute_interval(item), True))
    return module_details

print(inspect_module('./docparse/extract.py'))