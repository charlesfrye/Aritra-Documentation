import parser

from demo import sample

doc_string = sample.__doc__
p_d = parser.parse_docstring(doc_string)

md_doc='''
[source](https://github.com/wandb/client/blob/master/wandb/apis/public.py#L172)

# Description:
{}

# Returns:
{}
'''.format(p_d['long_description'], p_d['returns'])

with open('doc.md', 'w') as f:
    f.write(md_doc)