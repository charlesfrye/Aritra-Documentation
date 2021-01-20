"""A tool to generate api_docs for TensorFlow2.

```
python generate2.py --output_dir=/tmp/out
```

Requires a local installation of `tensorflow_docs`:

```
pip install git+https://github.com/tensorflow/docs
```
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pathlib
from os import path

from absl import app
from absl import flags

import wandb

from tensorflow_docs.api_generator import doc_controls
from tensorflow_docs.api_generator import generate_lib

# # patch all the values in `__all__`
# wandb.__all__ = [item_name for item_name in dir(wandb)]

FLAGS = flags.FLAGS

flags.DEFINE_string(
    "code_url_prefix",
    "/code/stable/wandb",
    "A url to prepend to code paths when creating links to defining code")

flags.DEFINE_string("output_dir", "/tmp/out",
                    "A directory, where the docs will be output to.")

flags.DEFINE_bool("search_hints", False,
                  "Include meta-data search hints at the top of each file.")

flags.DEFINE_string(
    "site_path", "",
    "The path prefix (up to `.../api_docs/python`) used in the "
    "`_toc.yaml` and `_redirects.yaml` files")

flags.DEFINE_bool("gen_report", False,
                  ("Generate an API report containing the health of the"
                   "docstrings of the public API."))


def build_docs(output_dir, code_url_prefix, search_hints, gen_report):
  """Build api docs for tensorflow v2.

  Args:
    output_dir: A string path, where to put the files.
    code_url_prefix: prefix for "Defined in" links.
    search_hints: Bool. Include meta-data search hints at the top of each file.
    gen_report: Bool. Generates an API report containing the health of the
      docstrings of the public API.
  """
#   try:
#     doc_controls.do_not_generate_docs(wandb.lightgbm)
#   except AttributeError:
#     pass
#   try:
#     doc_controls.do_not_generate_docs(wandb.sacred)
#   except AttributeError:
#     pass
#   try:
#     doc_controls.do_not_generate_docs(wandb.sklearn)
#   except AttributeError:
#     pass
#   try:
#     doc_controls.do_not_generate_docs(wandb.pandas)
#   except AttributeError:
#     pass
#   try:
#     doc_controls.do_not_generate_docs(wandb.agents)
#   except AttributeError:
#     pass
#   try:
#     doc_controls.do_not_generate_docs(wandb.sdk.internal)
#   except AttributeError:
#     pass

  doc_generator = generate_lib.DocGenerator(
      root_title="Weights&Biases",
      py_modules=[("wandb", wandb)],
      base_dir=path.dirname(wandb.__file__),
      search_hints=search_hints,
      code_url_prefix=path.dirname(wandb.__file__),
      site_path=FLAGS.site_path,
      gen_report=gen_report,
  )

  doc_generator.build(output_dir)

def main(argv):
  del argv
  build_docs(
      output_dir=FLAGS.output_dir,
      code_url_prefix=FLAGS.code_url_prefix,
      search_hints=FLAGS.search_hints,
      gen_report=FLAGS.gen_report,)


if __name__ == "__main__":
  app.run(main)
