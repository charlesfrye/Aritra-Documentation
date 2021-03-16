# Important Files
- `generate.py`: Generic documentation generator for wandb
- `docgen_cli.py`: Documentation generator for wandb CLI

## `generate.py`
The following is a road map of how to generate documentation like tensorflow.

### Steps
1. `pip install git+git://github.com/ariG23498/docs.git@wandb-docs` This installs the modified `tensorflow_docs`. The modifications are minor templating changes.
2. `pip install git+git://github.com/wandb/client.git@<git_hash>` This will install the wandb version that we want.
3. `python generate.py` creates the documentation. Here the script will ask for the `git_hash`. Please provide the git hash so that the source links do not change.

### Outputs
A folder named `library` in the same folder as the code. The files in the `library` folder are the generated markdown.

### Requirements
- `tensorflow_docs`
- `wandb`

## `docgen_cli.py`

### Usage
```bash
$ python docgen_cli.py
```

### Outputs
A file named `cli.md` in the same folder as the code. The file is the generated markdown for the CLI.

### Requirements
- `python >= 3.8`
- `wandb`
