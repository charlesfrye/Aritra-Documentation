"""
This module is used to extract a docstring from the source.
"""

# Global imports
import re
import os


class PyExtract(object):
    """
    Class for extracting docstrings.

    Attributes:
        source_code: A string that contains the source code that has been 
            read from the path specified.
        query: A string that is the serach term. The search is specified
            in the form of `.` for module, `Class` for class, `function`
            for function and `Class.method` for method.
        classname: Holds the class name of the query.
        funcname: Holds the function/method name of the query.
        dtype: Holds the type of the query. One of these 
            [`module`, `class`, `method`, `function`]
    """

    def __init__(self, source_code):
        """
        Initializer for Extract.

        Arguments:
            source_code: A string containing the text to extract docstrings
                from.
        """
        self.source_code = source_code
        self.query = ''
        self.classname = ''
        self.funcname = ''
        self.dtype = ''
        # The ids are used to index the group from the regex findall
        self.ids = {
            'class': 0,
            'function': 1,
            'signature': 2,
            'indent': 3,
            'docstring': 4,
            'body': 5,
            'return_annotation': 100
        }
        # This dictionary contains keywords that describe if a function should
        # start with 'def', and if the docstring that comes after the function
        # should be enclosed with """.
        self.keywords = {
            'function': 'def ',
            'docstring': '"""',
            'signature_end': ':',
            'token_split': 'def ',
        }
        self.function_keyword = 'def '
        self.docstring_keyword = '"""'
        # Handle multiple functions (typically function overloads) by splitting
        # text for each function. The key `token_split` in `self.keywords`.
        # determines the regex for the splitting.
        self.split = 1
    
    def get_matches(self, pattern):
        """
        Apply regex pattern for finding functions, classes, etc. 

        Args:
            pattern: The pattern to search for.

        Raises:
            NameError: if no matches are found. 

        Returns:
            The matches found.
            

        """
        matches = re.compile(pattern, re.M).findall(self.source_code)
        if not matches:
            raise NameError(
                f'Unable to extract docstring for `{self.query}`')
        return matches

    def extract(self, query):
        """
        Routes to the specific extract method

        Arguments:
            query : The docstring to search for. The search is specified in the
                form of `Class.method`, or `Class`, or `function`, or `.` to 
                search for the module docstring.

        Returns:
            A dictionary that matches the description given by `PyExtract.find`.

        """

        self.query = query
        self.classname, self.funcname, self.dtype = get_names(query)
        types = {
            'class': self.extract_class,
            'method': self.extract_method,
            'function': self.extract_function,
            'module': self.extract_module
        }

        return types[self.dtype]()

    def extract_function(self):
        """
        The functions extracted are module functions.

        Returns:
            A dictionary that matches the description given by `PyExtract.find`.
        """
                 #  ^\s*                         - start with zero or more space
                 #      (%s)                     - capture name of function
                 #          (                    - start of capture
                 #           \([\w\W]*?\)        - the arguments
        pattern =(r'^\s*(%s)(\([\w\W]*?\)' % self.funcname +
                 #  \s*                          - zero of more spaces
                 #     (?:                       - start non capturing parantesis
                 #        ->                     - -> pattern
                 #          \s*                  - zero of more spaces
                 #             ([\w\W]+)         - return attribute 
                 #                      )        - end non capturing parantesis
                 #                       ?       - zero or one return attribute 
                 #                        )      - end of capture
                 #                         %s    - : pattern
                 #                           \n+ - one or more end line
                  r'\s*(?:->\s*([\w\W]+))?)%s\n+' % self.keywords['signature_end'] +
                 #  (\s+)                               - number of indents for docstring
                 #       %s                             - """ pattern
                 #         ([\w\W]*?)                   - capture the doctring
                 #                   %s                 - """ pattern
                 #                     \n+              - one or more end line
                 #                        ((\4.*\n+)+)? - indent and code
                  r'(\s+)%s([\w\W]*)?%s\n+((:?\4.*\n+)+)?' % 
                  (self.keywords['docstring'],
                  self.keywords['docstring'],))

        ids = {
            'class': 100,
            'function': 0,
            'signature': 1,
            'return_annotation': 2,
            'indent': 3,
            'docstring': 4,
            'body': 5
        }
        return self.findall(pattern, ids)

    def extract_class(self):
                    #^\s*                                                   - zero or more space
                    #    class                                              - class pattern
                    #         \s+                                           - one or more space
                    #            (%s)                                       - capture classs name
                    #                ()                                     - capture nothing
                    #                  (\(\w*\))?                           - everything in ()
                    #                            %s                         - : pattern
                    #                              \n+                      - one or more endline
                    #                                 (\s+)                 - capture indents
                    #                                      %s               - """ pattern
                    #                                        ([\w\W]*?)     - docstring capture
                    #                                                  %s   - """ pattern
                    #                                                    () - capture nothing
        pattern = (r'^\s*class\s+(%s)()(\(\w*\))?%s\n(\s+)%s([\w\W]*?)%s()' %
                   (self.classname,
                   self.keywords['signature_end'],
                   self.keywords['docstring'],
                   self.keywords['docstring'],))
        return self.find(pattern)

    def extract_method(self):
                  #  class                                  - class pattern
                  #       \s+                               - one or more space
                  #          (%s)                           - capture classname
                  #              \(?\w*\)?                  - capture everything in ()
                  #                       %s                - : pattern
                  #                         [\n\s]+         - one or more endline or space
                  #                                [\w\W]*? - everything non greedy
        pattern = (r'class\s+(%s)\(?\w*\)?%s[\n\s]+[\w\W]*?' % (self.classname, self.keywords['signature_end']) +
                  #  [\n\s]+                                - one or more, endline or space
                  #         def                             - def pattern
                  #            \s+                          - one or more space
                  #               (%s)                      - capture function name
                  #                   (\(\s*self[\w\W]*?\)  - everything in (self)
                   r'[\n\s]+def\s+(%s)(\(\s*self[\w\W]*?\)' % self.funcname +
                  #  \s*                                    - zero or more space
                  #     (?:                                 - non capture start
                  #        ->                               - -> pattern
                  #          \s*                            - zero or more space
                  #             ([\w\W]+)                   - one or more characters
                  #                      )                  - non capture end
                  #                       ?)                - zero or one previous pattern
                  #                         %s              - : pattern
                  #                           \n+           - one or more end line
                   r'\s*(?:->\s*([\w\W]+))?)%s\n+' % self.keywords['signature_end'] +
                  #  (\s+)                                  - capture indents
                  #       %s                                - """ pattern
                  #         ([\w\W]*?)                      - charaters capture non greedy
                  #                   %s                    - """ patter
                  #                     \n+                 - one or more endline
                  #                        ((?:\4.*\n+)+)?  - the source code
                   r'(\s+)%s([\w\W]*?)%s\n+((?:\4.*\n+)+)?' %
                   (self.keywords['docstring'],
                   self.keywords['docstring'],))
        ids = {
            'class': 0,
            'function': 1,
            'signature': 2,
            'return_annotation': 3,
            'indent': 4,
            'docstring': 5,
            'body': 6
        }
        return self.find(pattern, ids)

    def extract_module(self):
                  # ()                         - capture nothing
                  #   ()                       - capture nothing
                  #     ()                     - capture nothing
                  #       ()                   - capture nothing
                  #         ^"""               - starts with """
                  #             ([\w\W]*?)     - capture the docstring non greedy
                  #                       """  - """ pattern
        pattern = r'()()()()^"""([\w\W]*?)"""'
        return self.find(pattern)

    def findall(self, pattern, ids=None):
        """
        Splits the source code into multiple strings and performs a search for
        each string. The idea is to handle text that contains multiple
        functions/methods and search each such function for a specific pattern.

        """
        out = []
        input_txt = self.source_code
        if self.split:
            matches = re.split(
                self.keywords['token_split'], input_txt, flags=re.M)
            for match in matches:
                self.source_code = match
                try:
                    out.append(self.find(pattern, ids))
                except:
                    continue
            self.source_code = input_txt
            if not out:
                raise NameError(
                    f'Unable to extract docstring for `{self.query}`'
                    )
            if len(out) == 1:
                return out[0]
            else:
                return out
        else:
            return self.find(pattern, ids)

    def find(self, pattern, ids=None):
        """
        Performs a search for a docstring that matches a specific pattern.

        Returns:
            dict: The return type is a dictionary with the following keys:
                * `class` :  The name of the class.
                * `function` : The name of the function/method.
                * `signature` : The signature of the function/method.
                * `docstring` : The docstring itself.
                * `type` : What type of construct the docstring is attached to.
                    This can be either `'module'`, `'class'`, `'method'`, or
                    `'function'`.
                * `label` : The search query string.
                * `args` : A dictionary containing signature arguments, and
                return type.

        Raises:
            NameError: This is exception is raised if the docstring cannot be
                extracted.
        """
        import textwrap
        try:
            from . import parse
        except:
            import parse
        matches = self.get_matches(pattern)

        if not ids:
            ids = self.ids

        out_list = []

        for match in matches:
            cls = get_match(match, ids['class'])
            function = get_match(match, ids['function'])
            signature = format_txt(get_match(match, ids['signature']))
            indent = len(get_match(match, ids['indent']))
            return_annotation = get_match(match, ids['return_annotation'])
            docstring = remove_indent(
                get_match(match, ids['docstring']), indent)
            if self.dtype == 'function' or self.dtype == 'method':
                source = textwrap.dedent(self.function_keyword + function +
                                         signature + ':' + return_annotation +
                                         '\n' + get_match(match, ids['body']))
            else:
                source = ''

            out = {}
            out['class'] = cls
            out['function'] = function
            out['signature'] = signature
            out['docstring'] = docstring
            out['return_annotation'] = return_annotation
            out['source'] = source
            out['type'] = self.dtype
            out['label'] = self.query
            # try:
            #     out['parsed_signature'] = parse.parse_signature(
            #         out['signature'])
            # except:
            #     pass
            out_list.append(out)

        if len(out_list) == 1:
            return out_list[0]
        else:
            return out_list



def extract(file_path, query):
    """
    Extracts a docstring from source.

    Arguments:
        filestr: A string that specifies filename of the source code to extract
            from.
        query: A string that specifies what type of docstring to extract.
            Can be one of these ['.', 'Class', 'Class.method', 'function']

    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            source_code = f.read()
        extractor = PyExtract(source_code)
    else:
        raise FileNotFoundError(
                    f'Unable to find `{file_path}`'
                    )
    return extractor.extract(query)
    

def get_names(query):
    """
    Extracts the module, class, function or method name from a query string.
    The query string is in the format `Class.function`.
    Functions starts with a lower case letter and classes starts
    with an upper case letter. For empty query we get a module.

    Arguments:
        query (str): The string to process.

    Returns:
        tuple: A tuple containing the class name, function name,
               and type. The class name or function name can be empty.

    """
    funcname = ''
    classname = ''
    dtype = ''

    members = query.split('.')
    if len(members) == 1:
        # Class or function
        term = members[0]
        if term[0].isupper():
            dtype = "class"
            classname = term
        else:
            dtype = "function"
            funcname = term
    elif len(members) == 2:
        # module or method
        if not members[0] and not members[1]:
            dtype = "module"
        else:
            dtype = 'method'
            classname, funcname = members
    else:
        raise ValueError(
            f'[FROM get_names]: Unable to parse: `{query}`'
        )

    return (classname, funcname, dtype)


def remove_indent(txt, indent):
    """
    Dedents a string by a certain amount.
    """
    lines = txt.split('\n')
    if lines[0] != '\n':
        header = '\n' + lines[0]
    else:
        header = ''
    return '\n'.join([header] + [line[indent:] for line in lines[1:]])


def get_match(match, index, default=''):
    """
    Returns a value from match list for a given index. In the list is out of
    bounds `default` is returned.

    """
    if index >= len(match):
        return default
    else:
        return match[index]


def format_txt(signature):
    """
    Remove excess spaces and newline characters.
    """
    return ' '.join(' '.join(signature.split('\n')).split())
