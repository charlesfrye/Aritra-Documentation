from mydocstring.extract import extract
from mydocstring import parse

import sys

filename = sys.argv[1]
query = sys.argv[2]

def setup_google(filename=filename, 
                 query=query, 
                 signature=None, 
                 config=None
                 ):
    match = extract(filename, query)
    google = parse.GoogleDocString(match['docstring'].lstrip('\n'), signature=signature,
                config=config)
    return google

google = setup_google(filename=filename, query=query)
docstr = google.parse()
for item in docstr:
    print(item)
    print()