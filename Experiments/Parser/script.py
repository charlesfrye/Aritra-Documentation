from parse import GoogleDocString
from extract import extract

# Extract the docstring
doc_dict = extract(
    filestr='wandb_init.py',
    query='func'
    )

# parse
google_doc = GoogleDocString(doc_dict['docstring'])

# parsed list
parsed_list = google_doc.parse(mark_code_blocks=True)

for element in parsed_list:
    print(element)