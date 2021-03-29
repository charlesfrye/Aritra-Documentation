# Documentation Generation

## `generate.py`

This script generates documentation for the `wandb` library based on a git commit hash in a format suitable for use with GitBook.

For help with this function, run

```text
python generate.py --help
```

### Steps

1. Run `pip install --upgrade git+git://github.com/wandb/client.git@<git_hash>` to install the version of`wandb` you wish to document.
2. Run `python generate.py --git_hash <git_hash>` to create the documentation.

### Outputs

1. A folder named `ref`. The files in the `ref` folder are the generated markdown. Use the `--output_dir` option to change where this is saved; by default it is in the same folder as the code.
2. A `SUMMARY.md` file for creating a GitBook sidebar containing the automatically-generated docs. This is based on a provided template file \(by default, `_SUMMARY.md` from this repo\).

### Requirements

*  `pip install git+git://github.com/ariG23498/docs.git@wandb-docs` 

