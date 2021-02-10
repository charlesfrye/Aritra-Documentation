# Documemtation Generation

The follwing is a road map of how to generate documentaion like tensorflow.

Steps:

1. `pip install git+https://github.com/ariG23498/docs@wandb-docs` This installs the modified `tensorflow_docs`. The modifications are minor templating changes.
2. `pip install git+https://github.com/ariG23498/client` This installs the modified `wandb` client package. The modifications are all about docstring changes. This does not have to do with any code change.
3. `python generate.py` creates the documentation.

