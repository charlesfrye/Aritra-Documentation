import re
import sys

# Used to demarcate the description from :param: or :returns:
PARAM_OR_RETURNS_REGEX = re.compile(":(?:param|returns)")
# Used to fetch the :returns:
RETURNS_REGEX = re.compile(":returns: (?P<doc>.*)", re.S)
# Used to fetch the :param parameter: :type type: documentation
PARAM_REGEX = re.compile(":param (?P<name>[\*\w]+): :type (?P<type>[\*\w]+): (?P<doc>.*?)"
                         "(?:(?=:param)|(?=:return)|(?=:raises)|\Z)", re.S)

def trim(docstring):
    """
    Strips the docstring
    Splits the doctstring into multiplte lines
    Strips the lines off of their indentation
    Aggregates the lines again to form an unindented text
    """
    if not docstring:
        return ""
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)

    # Return a single string:
    return "\n".join(trimmed)


def reindent(string):
    '''
    Reindents the string
    Used for cases like :returns: Doc
    '''
    return "\n".join(l.strip() for l in string.strip().split("\n"))

def parse_docstring(docstring):
    """Parse the docstring into its components.
    :returns: a dictionary of form
              {
                  "short_description": ...,
                  "long_description": ...,
                  "params": [
                      {"name": ..., "type": ..., "doc": ...}, ...],
                  "returns": ...
              }
    """
    # Initiaize all the values
    short_description = long_description = returns = ""
    params = []

    if docstring:
        docstring = trim(docstring)

        lines = docstring.split("\n", 1)
        short_description = lines[0]
        # Check if long description is present
        if len(lines) > 1:
            long_description = lines[1].strip()

            params_returns_desc = None

            match = PARAM_OR_RETURNS_REGEX.search(long_description)
            # Check if docstring has parameters of returns
            if match:
                long_desc_end = match.start()
                params_returns_desc = long_description[long_desc_end:].strip()
                long_description = long_description[:long_desc_end].rstrip()
            # Check if docstring has parameters of returns
            if params_returns_desc:
                params = [
                    {"name": name, "type": ty, "doc": trim(doc)}
                    for name, ty, doc in PARAM_REGEX.findall(params_returns_desc)
                ]

                match = RETURNS_REGEX.search(params_returns_desc)
                if match:
                    returns = reindent(match.group("doc"))

    return {
        "short_description": short_description,
        "long_description": long_description,
        "params": params,
        "returns": returns
    }