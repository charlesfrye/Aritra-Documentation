import ast
import _ast
import sys
import tokenize

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
    module_classes = [_ for _ in tree.body if isinstance(_, _ast.ClassDef)]
    module_functions = [_.name for _ in tree.body if isinstance(_, _ast.FunctionDef)]
    module_classes = [(c.name, [_.name for _ in c.body if isinstance(_, _ast.FunctionDef)]) for c in module_classes]
    return (module_classes, module_functions)

filename = sys.argv[1]
module_classes, module_functions = inspect_module(filename)
print('**MODULE FUNCTIONS**')
for func_name in module_functions:
    print(func_name)

print('**MODULE CLASSES with METHODS**')
for class_name, method_names in module_classes:
    print(class_name)
    for method_name in method_names:
        print('  {}'.format(method_name))
