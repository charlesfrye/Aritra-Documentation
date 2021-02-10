"""A tool to generate api_docs for wandb

```
python generate.py --output_dir=docs
```

Requires a local installation of `tensorflow_docs`:

```
pip install git+https://github.com/tensorflow/docs
```
"""
from os import path, walk, getcwd, remove

import wandb

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import generate_lib

def build_docs(name_pair,output_dir,code_url_prefix, search_hints, gen_report):
    """Build api docs for w&b.
    
    Args:
        name_pair: Name of the pymodule
        output_dir: A string path, where to put the files.
        code_url_prefix: prefix for "Defined in" links.
        search_hints: Bool. Include meta-data search hints at the top of each file.
        gen_report: Bool. Generates an API report containing the health of the
            docstrings of the public API.
    """
    for cls in [wandb.data_types.WBValue, wandb.data_types.Media, wandb.data_types.BatchableMedia]:
        doc_controls.decorate_all_class_attributes(
            decorator=doc_controls.do_not_doc_in_subclasses,
            cls=cls,
            skip=["__init__"])

    doc_generator = generate_lib.DocGenerator(
        root_title="W&B",
        py_modules=[name_pair],
        base_dir=path.dirname(wandb.__file__),
        search_hints=search_hints,
        code_url_prefix=code_url_prefix,
        site_path="",
        gen_report=gen_report,
        yaml_toc=False)

    doc_generator.build(output_dir)


if __name__== "__main__":
    CODE_URL_PREFIX = "https://www.github.com/wandb/client/tree/master/wandb"

    wandb_classes = [
        'Artifact'
        ]

    wandb.__all__ = wandb_classes

    build_docs(
        name_pair=("Library", wandb),
        output_dir="Platform",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False)
    
    wandb.Api = wandb.apis.public.Api
    wandb.Projects = wandb.apis.public.Projects
    wandb.Project = wandb.apis.public.Project
    wandb.Runs = wandb.apis.public.Runs
    wandb.Run = wandb.apis.public.Run
    wandb.Sweep = wandb.apis.public.Sweep
    wandb.Files = wandb.apis.public.Files
    wandb.File = wandb.apis.public.File
    wandb.QueryGenerator = wandb.apis.public.QueryGenerator
    wandb.ArtifactType = wandb.apis.public.ArtifactType
    wandb.ArtifactCollection = wandb.apis.public.ArtifactCollection
    wandb.Artifact = wandb.apis.public.Artifact
    wandb.ArtifactVersions = wandb.apis.public.ArtifactVersions
    wandb_api_doc = [
        'Api',
        'Projects',
        'Project',
        'Runs',
        'Run',
        'Sweep',
        'Files',
        'File',
        'QueryGenerator',
        'ArtifactType',
        'ArtifactCollection',
        'Artifact',
        'ArtifactVersions',
    ]
    wandb.__all__ = wandb_api_doc

    build_docs(
        name_pair=("Public Api",wandb),
        output_dir="Platform/Library",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False)


    wandb.settings = wandb.wandb_sdk.Settings
    wandb_run = [
        'init',
        'log',
        'config',
        'summary',
        'login',
        'alert',
        'settings']
    
    wandb.__all__ = wandb_run
    try:
        doc_controls.do_not_generate_docs(wandb.settings.Console)
    except AttributeError:
        pass
    try:
        doc_controls.do_not_generate_docs(wandb.settings.Source)
    except AttributeError:
        pass
    build_docs(
        name_pair=("Run",wandb),
        output_dir="Platform/Library",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False)

    wandb_datatypes = [
        'Image',
        'Plotly',
        'Video',
        'Audio',
        'Table',
        'Html',
        'Object3D',
        'Molecule',
        'Histogram',]

    wandb.__all__ = wandb_datatypes

    build_docs(
        name_pair=("Data Types",wandb),
        output_dir="Platform/Library",
        code_url_prefix=CODE_URL_PREFIX,
        search_hints=False,
        gen_report=False)

    # Remove the unwanted files
    # all_symbols and _api.cache.md
    directory = getcwd()
    for root, folder, file_names in walk("Platform"):
        if "all_symbols.md" in file_names:
            remove(f"{root}/all_symbols.md")
        if "_api_cache.json" in file_names:
            remove(f"{root}/_api_cache.json")