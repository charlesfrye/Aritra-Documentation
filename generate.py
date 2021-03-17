"""A tool to generate api_docs for wandb

For help, run:

python generate.py --help
"""
import argparse
import os

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import generate_lib
import wandb

from docgen_cli import cli_gen

DIRNAME = "library"


def main(args):
    git_hash = args.git_hash
    output_dir = args.output_dir
    code_url_prefix = "/".join([args.repo, "tree", f"{git_hash}", args.prefix])

    configure_doc_hiding()

    # each of these operates by changing the __all__
    #  attribute of the wandb module, populating it with
    #  the relevant objects and then generating docs.

    build_library_docs(git_hash, code_url_prefix, output_dir)
    build_datatype_docs(git_hash, code_url_prefix, output_dir)
    build_api_docs(git_hash, code_url_prefix, output_dir)

    # convert generate_lib output to GitBook format
    rename_to_readme(output_dir)
    library_dir = os.path.join(output_dir, DIRNAME)
    filter_files(library_dir, ["all_symbols.md", "_api_cache.json"])
    clean_names(library_dir)

    # Create the CLI docs
    cli_gen()

    # fill the SUMMARY.md with generated doc files,
    #  based on template in _SUMMARY.md
    populate_summary(DIRNAME)


def build_docs(name_pair, output_dir, code_url_prefix, search_hints, gen_report):
    """Build api docs for W&B.

    Args:
        name_pair: Name of the pymodule
        output_dir: A string path, where to put the files.
        code_url_prefix: prefix for "Defined in" links.
        search_hints: Bool. Include meta-data search hints at the top of each file.
        gen_report: Bool. Generates an API report containing the health of the
            docstrings of the public API.
    """

    doc_generator = generate_lib.DocGenerator(
        root_title="W&B",
        py_modules=[name_pair],
        base_dir=os.path.dirname(wandb.__file__),
        search_hints=search_hints,
        code_url_prefix=code_url_prefix,
        site_path="",
        gen_report=gen_report,
        yaml_toc=False,
    )

    doc_generator.build(output_dir)


def populate_summary(docgen_folder: str, template_file: str = "_SUMMARY.md",
                     output_path: str = "SUMMARY.md") -> None:
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
        output_path: str. Location at which to write the final markdown.
    """

    with open(template_file, "r") as f:
        doc_structure = f.read()

    autodoc_markdown = walk_autodoc(docgen_folder)

    doc_structure = doc_structure.format(autodoc=autodoc_markdown)

    with open(output_path, "w") as f:
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


def build_library_docs(git_hash, code_url_prefix, output_dir):
    wandb.Run = wandb.sdk.wandb_run.Run
    wandb_classes = ["Artifact", "config", "summary", "init",
                     "login", "Run"]

    wandb.__all__ = wandb_classes
    wandb.__doc__ = """\n"""

    try:
        doc_controls.do_not_generate_docs(wandb.Run.__exit__)
    except AttributeError:
        pass
    try:
        doc_controls.do_not_generate_docs(wandb.Run.__enter__)
    except AttributeError:
        pass

    build_docs(
        name_pair=(DIRNAME, wandb),
        output_dir=output_dir,
        code_url_prefix=code_url_prefix,
        search_hints=False,
        gen_report=False,
    )


def build_datatype_docs(git_hash, code_url_prefix, output_dir):

    wandb_datatypes = ["Image", "Plotly", "Video", "Audio", "Table",
                       "Html", "Object3D", "Molecule", "Histogram"]

    wandb.__all__ = wandb_datatypes
    wandb.__doc__ = """\n"""
    build_docs(
        name_pair=("data-types", wandb),
        output_dir=os.path.join(output_dir, DIRNAME),
        code_url_prefix=code_url_prefix,
        search_hints=False,
        gen_report=False,
    )


def build_api_docs(git_hash, code_url_prefix, output_dir):

    wandb.Api = wandb.apis.public.Api
    wandb.Projects = wandb.apis.public.Projects
    wandb.Project = wandb.apis.public.Project
    wandb.Runs = wandb.apis.public.Runs
    wandb.Run = wandb.apis.public.Run
    wandb.Sweep = wandb.apis.public.Sweep
    wandb.Files = wandb.apis.public.Files
    wandb.File = wandb.apis.public.File
    wandb.Artifact = wandb.apis.public.Artifact
    wandb_api_doc = ["Api", "Projects", "Project", "Runs", "Run",
                     "Sweep", "Files", "File", "Artifact"]

    wandb.__all__ = wandb_api_doc
    wandb.__doc__ = """
    Use the Public API to export or update data that you have saved to W&B.
    Before using this API, you'll want to log data from your script — check the [Quickstart](../quickstart.md) for more details.

    **Use Cases for the Public API**

    * **Export Data**: Pull down a dataframe for custom analysis in a Jupyter Notebook. Once you have explored the data, you can sync your findings by creating a new analysis run and logging results, for example: `wandb.init(job_type="analysis")`
    * **Update Existing Runs**: You can update the data logged in association with a W&B run. For example, you might want to update the config of a set of runs to include additional information, like the architecture or a hyperparameter that wasn't originally logged.

    See the [Generated Reference Docs](../ref/public-api/) for details on available functions.
    """
    build_docs(
        name_pair=("public-api", wandb),
        output_dir=os.path.join(output_dir, DIRNAME),
        code_url_prefix=code_url_prefix,
        search_hints=False,
        gen_report=False,
    )


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


def configure_doc_hiding():

    # avoid documenting internal methods
    #  that are defined in basic datatypes and apis

    deco = doc_controls.do_not_doc_in_subclasses
    base_classes = [wandb.data_types.WBValue,
                    wandb.data_types.Media,
                    wandb.data_types.BatchableMedia,
                    wandb.apis.public.Paginator]

    for cls in base_classes:
        doc_controls.decorate_all_class_attributes(decorator=deco, cls=cls, skip=["__init__"])


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
