"""A tool to generate api_docs for wandb

```
python generate.py --output_dir=docs
```

Requires a local installation of `tensorflow_docs`:

```
pip install git+https://github.com/tensorflow/docs
```
"""
import os

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import generate_lib
import wandb

from docgen_cli import cli_gen


def main(git_hash):
    code_url_prefix = f"https://www.github.com/wandb/client/tree/{git_hash}/wandb"

    build_library_docs(git_hash, code_url_prefix)
    build_datatype_docs(git_hash, code_url_prefix)
    build_api_docs(git_hash, code_url_prefix)

    directory = os.getcwd()

    # convert generate_lib output to GitBook format
    filter_files(directory, ["all_symbols.md", "_api_cache.json"])
    rename_to_readme(directory)
    clean_names(directory, "library")

    # Create the CLI docs
    cli_gen()

    # fill the SUMMARY.md with generated doc files,
    #  based on template in _SUMMARY.md
    populate_summary("library")


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
    # This is to help not document the parent class methods
    for cls in [
        wandb.data_types.WBValue,
        wandb.data_types.Media,
        wandb.data_types.BatchableMedia,
        wandb.apis.public.Paginator,
    ]:
        doc_controls.decorate_all_class_attributes(
            decorator=doc_controls.do_not_doc_in_subclasses, cls=cls, skip=["__init__"]
        )

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
    by filling in the template_file a the {autodoc} location.

    GitBook uses a `SUMMARY.md` file to determine which.


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
    """
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
        if file_name == "README.md":
            continue
        short_name = file_name.split(".")[0]
        file_markdown = indentation + f"  * [{short_name}]({root}/{file_name})"
        file_markdowns.append(file_markdown)

    return file_markdowns


def build_library_docs(git_hash, code_url_prefix):
    wandb.Run = wandb.sdk.wandb_run.Run
    wandb_classes = [
        "Artifact",
        "config",
        "summary",
        "init",
        "login",
        "Run",
    ]
    wandb.__all__ = wandb_classes
    wandb.__doc__ = """
    """
    try:
        doc_controls.do_not_generate_docs(wandb.Run.__exit__)
    except AttributeError:
        pass
    try:
        doc_controls.do_not_generate_docs(wandb.Run.__enter__)
    except AttributeError:
        pass
    build_docs(
        name_pair=("library", wandb),
        output_dir=".",
        code_url_prefix=code_url_prefix,
        search_hints=False,
        gen_report=False,
    )


def build_datatype_docs(git_hash, code_url_prefix):

    wandb_datatypes = [
        "Image",
        "Plotly",
        "Video",
        "Audio",
        "Table",
        "Html",
        "Object3D",
        "Molecule",
        "Histogram",
    ]
    wandb.__all__ = wandb_datatypes
    wandb.__doc__ = """
    """
    build_docs(
        name_pair=("data-types", wandb),
        output_dir="./library",
        code_url_prefix=code_url_prefix,
        search_hints=False,
        gen_report=False,
    )


def build_api_docs(git_hash, code_url_prefix):

    wandb.Api = wandb.apis.public.Api
    wandb.Projects = wandb.apis.public.Projects
    wandb.Project = wandb.apis.public.Project
    wandb.Runs = wandb.apis.public.Runs
    wandb.Run = wandb.apis.public.Run
    wandb.Sweep = wandb.apis.public.Sweep
    wandb.Files = wandb.apis.public.Files
    wandb.File = wandb.apis.public.File
    wandb.Artifact = wandb.apis.public.Artifact
    wandb_api_doc = [
        "Api",
        "Projects",
        "Project",
        "Runs",
        "Run",
        "Sweep",
        "Files",
        "File",
        "Artifact",
    ]
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
        output_dir="./library",
        code_url_prefix=code_url_prefix,
        search_hints=False,
        gen_report=False,
    )


def rename_to_readme(directory):
    # Moving all the folder-level md to respective folders
    os.rename(f"{directory}/library.md", f"{directory}/library/README.md")
    os.rename(
        f"{directory}/library/data-types.md",
        f"{directory}/library/data-types/README.md",
    )
    os.rename(
        f"{directory}/library/public-api.md",
        f"{directory}/library/public-api/README.md",
    )


def clean_names(directory, folder):
    """Converts names to lower case and removes spaces
    """
    for root, folder, file_names in os.walk(folder):
        for name in file_names:
            if name == "README.md":
                short_name = name
            else:
                short_name = name.replace(" ", "-").lower()
            os.rename(f"{directory}/{root}/{name}", f"{directory}/{root}/{short_name}")


def filter_files(directory, files_to_remove):
    for root, folder, file_names in os.walk(directory):
        if "all_symbols.md" in file_names:
            os.remove(f"{root}/all_symbols.md")
        if "_api_cache.json" in file_names:
            os.remove(f"{root}/_api_cache.json")


if __name__ == "__main__":
    git_hash = "3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c"

    main(git_hash)
