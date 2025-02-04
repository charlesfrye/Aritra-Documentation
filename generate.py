"""A tool to generate api_docs for wandb

For help, run:

python generate.py --help
"""
import argparse
import os

import docgen_cli
import docgen_lib

DIRNAME = docgen_lib.DIRNAME  # directory name for autodocs


def main(args):
    git_hash = args.git_hash
    output_dir = args.output_dir
    code_url_prefix = "/".join([args.repo, "tree", f"{git_hash}", args.prefix])

    docgen_lib.build(git_hash, code_url_prefix, output_dir)

    # convert generate_lib output to GitBook format
    rename_to_readme(output_dir)
    library_dir = os.path.join(output_dir, DIRNAME)
    filter_files(library_dir, ["all_symbols.md", "_api_cache.json"])
    clean_names(library_dir)

    # Create the CLI docs
    docgen_cli.build(library_dir)

    # fill the SUMMARY.md with generated doc files,
    #  based on template in _SUMMARY.md
    populate_summary(DIRNAME, output_dir=output_dir)


def populate_summary(docgen_folder: str, template_file: str = "_SUMMARY.md",
                     output_dir: str = ".") -> None:
    """Populates the output file with generated file names
    by filling in the template_file at the {autodoc} location.

    GitBook uses a `SUMMARY.md` file to determine which
    files to show in the sidebar. When using autodoc,
    we must generate this partly programmatically.

    Args:
        docgen_folder: str. The root folder that contains
            the generated docs.
        template_file: str. A markdown template that contains
            the rest of the SUMMARY.md.
        output_dir: str. Directory into which to write the final
            SUMMARY.md file.
    """

    with open(template_file, "r") as f:
        doc_structure = f.read()

    autodoc_markdown = walk_autodoc(docgen_folder)

    doc_structure = doc_structure.format(autodoc=autodoc_markdown)

    with open(os.path.join(output_dir, "SUMMARY.md"), "w") as f:
        f.write(doc_structure)


def walk_autodoc(folder: str) -> str:
    """Walks a folder, pulls out all of the markdown files,
    formats their names into markdown strings with appropriate links
    and formatting for a GitBook SUMMARY.md, then returns that block of markdown.
    """

    autodoc_markdowns = []
    indent = 0
    for path, dirs, files in os.walk(folder):
        is_subdir = "/" in path
        if is_subdir:
            components = path.split("/")
            indent = len(components)
            name = components[-1]
        else:
            name = path
        autodoc_markdowns.append(" " * indent + f"* [{name}]({path}/README.md)")

        autodoc_markdowns.extend(add_files(files, path, indent))

    autodoc_markdown = "\n".join(autodoc_markdowns)

    return autodoc_markdown


def add_files(files: list, root: str, indent: int) -> list:
    file_markdowns = []
    indentation = " " * indent
    for file_name in files:
        if file_name == "README.md" or not file_name.endswith(".md"):
            continue
        short_name = file_name.split(".")[0]
        file_markdown = indentation + f"  * [{short_name}]({root}/{file_name})"
        file_markdowns.append(file_markdown)

    return file_markdowns


def rename_to_readme(directory):
    """Moves all the folder-level markdown files into
    their respective folders, as a README."""

    for root, folders, file_names in os.walk(directory):
        for file_name in file_names:
            raw_file_name, suffix = file_name[:-3], file_name[-3:]
            if suffix == ".md" and raw_file_name in folders:
                os.rename(os.path.join(f"{root}", file_name),
                          os.path.join(f"{root}", raw_file_name, "README.md"))


def clean_names(directory):
    """Converts names to lower case and removes spaces
    """
    for root, folders, file_names in os.walk(directory):
        for name in file_names:
            if name == "README.md":
                short_name = name
            else:
                short_name = name.replace(" ", "-").lower()
            os.rename(os.path.join(f"{root}", f"{name}"),
                      os.path.join(f"{root}", f"{short_name}"))


def filter_files(directory, files_to_remove):
    for root, _, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name in files_to_remove:
                os.remove(os.path.join(f"{root}", f"{file_name}"))


def get_args():
    parser = argparse.ArgumentParser(
        description="Generate documentation for the wandb library and CLI.")
    parser.add_argument(
        "--git_hash", type=str, default="3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c",
        help="Hash for the git commit to base the docs on. "
        + "Ensures that the source code is properly linked.")
    parser.add_argument(
        "--repo", type=str, default="https://www.github.com/wandb/client",
        help="Repo to link for source code.")
    parser.add_argument(
        "--prefix", type=str, default="wandb",
        help="Folder within repo where wandb library is located.")
    parser.add_argument(
        "--output_dir", type=str, default=os.getcwd(),
        help="Folder into which to place folder library/ containing results.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    main(args)
