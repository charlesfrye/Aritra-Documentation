from docspec_python import parse_python_module
from docspec import dump_module
import re
import click

PATTERN = re.compile(r'help= ?"(.*?)"')
SOURCE_CODE = "https://github.com/ariG23498/Aritra-Documentation/blob/master/"
TEMPLATE = """
{}
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)]({})

{}

{}

{}

{}

{}

{}

{}
""".strip()

def parse_class(class_member, filename, module_name):
    class_name = class_member["name"]
    class_location = class_member["location"]["lineno"]
    class_members = class_member["members"]
    doc = ""
    if "docstring" in class_member.keys():
        doc = module_dict["docstring"]
    parent = ""
    if "bases" in class_member.keys():
        parent = ', '.join(class_member["bases"])
    with open(f'{module_name}.md', 'a') as fp:
        text = TEMPLATE.format(
            f'# {class_name}', #header
            f'{SOURCE_CODE}{filename}#L{class_location}', #source file in repo: https://github.com/ariG23498/Aritra-Documentation/blob/master/____
            f'`class {class_name}({parent}):`', #function signature: extract['source']
            doc, #summary
            "", #table_args 
            "", #table_att
            "", #hint
            "", #returns
            "" #example
        )
        fp.write(text)
    # Iterate over the class members and parse the methods
    for member in class_members:
         if member["type"] == "function":
            parse_func(member, filename, module_name, level=2)

def parse_func(func_member, filename, module_name, level=1):
    func_name = func_member["name"]
    name = f'# {func_name}' if level==1 else f'## {func_name}'
    func_location = func_member["location"]["lineno"]
    func_arg = ',\n'.join([x["name"] for x in func_member["args"]])
    doc = ""
    if "docstring" in func_member.keys():
        doc = func_member["docstring"]
    help_table = ""
    if "decorations" in func_member.keys():
        help_table = ""
        decorations = func_member["decorations"]
        for decoration in decorations:
            help_name = ""
            help_desc="None"
            if "args" in decoration.keys():
                help_name = decoration["args"][1:-2].split(',')[0].strip()
                if PATTERN.match(help_name):
                    help_name = ""
                help_desc = ' '.join(PATTERN.findall(decoration["args"]))
                help_table += """|{}|{}|\n""".format(help_name,help_desc)
        if help_table != "":
            help_table = """| **Options** | **Help** |\n|:--|:--|\n""" + help_table
    with open(f'{module_name}.md', 'a') as fp:
        text = TEMPLATE.format(
            f'{name}', #header
            f'{SOURCE_CODE}{filename}#L{func_location}', #source file in repo: https://github.com/ariG23498/Aritra-Documentation/blob/master/____
            f'`def {func_name}({func_arg}):`', #function signature: extract['source']
            doc, #summary
            help_table, #table_args 
            "", #table_att
            "", #hint
            "", #returns
            "" #example
        )
        fp.write(text)
            

@click.command()
@click.option("--filename", "-f", help="Name of the cli filename.")
def main(filename):
    # Turns the module into a dictionary
    module_dict = dump_module(parse_python_module(filename))
    module_name = module_dict["name"]
    module_location = module_dict["location"]["lineno"]
    module_members = module_dict["members"]
    doc = ""
    if "docstring" in module_dict.keys():
        doc = module_dict["docstring"]
    with open(f'{module_name}.md', 'w') as fp:
        text = TEMPLATE.format(
            f'# {module_name}', #header
            f'{SOURCE_CODE}{filename}#L{module_location}', #source file in repo: https://github.com/ariG23498/Aritra-Documentation/blob/master/____
            "", #function signature: extract['source']
            doc, #summary
            "", #table_args 
            "", #table_att
            "", #hint
            "", #returns
            "" #example
        )
        fp.write(text)
    # Iterate over the module members
    for member in module_members:
        if member["type"] == "class":
            parse_class(member, filename, module_name)
        elif member["type"] == "function":
            parse_func(member, filename, module_name)

if __name__ == "__main__":
    main()