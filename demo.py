"""
Module docstring
"""

def function_with_docstring(arg1, arg2=True):
    """Short description.
    Example of a function with a doc string.

    Some more details.

    Args:
        arg1(type): description for arg1.
        arg2 : description for arg2
            that spans multiple lines.

    Returns:
        bool: `True` or `False`. Defaults to `True`.

        The return section can also have a detailed description that spans
        multiple lines. It is important that this description is indented.

    """
    pass

class ExampleOldClass:
    """
    An example of a docstring for an old-style class.

    Some more details
    """

    def __init__(self,
                 arg1,
                 arg2):
        """
        Description of the __init__ function.

        Some more details. Documentation for `arg1` is missing on purpose. 

        Arguments:
            arg2 : description for arg2.

        Raises:
            NameError: Error will occur
        
        Examples:
            ```
            print('hello world')
            ```
        """
        pass

    def method_with_docstring(self, arg1, arg2):
        """
        Description of a method.

        Some more details.
        
        Arguments:
            arg1(type) : description for arg1.
            arg2 : description for arg1.

        """
        pass
    
class ExampleNewClass(object):
    """
    An example of a docstring for a new-style class.

    Some more details.

    """
    def __init__(self):
        """
        Example of a docstring for the init function.

        Some more details.
        """
        pass
    
    def method_with_new_line_before_self(
            self):
        """
        Method with a new line before `self`.
        """
        pass