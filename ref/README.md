# API Reference

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/__init__.py)

Wandb is a library to help track machine learning experiments.

For more information on wandb see [https://docs.wandb.com](https://docs.wandb.com).

The most commonly used functions/objects are:

* wandb.init — initialize a new run at the top of your training script
* wandb.config — track hyperparameters
* wandb.log — log metrics over time within your training loop
* wandb.save — save files in association with your run, like model weights
* wandb.restore — restore the state of your code when you ran a given run

For examples usage, see github.com/wandb/examples

## Classes

[`class Api`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/api.md): Used for querying the wandb server.

[`class Audio`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/audio.md): Wandb class for audio clips.

[`class Graph`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/graph.md): Wandb class for graphs

[`class Histogram`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/histogram.md): wandb class for histograms.

[`class Html`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/html.md): Wandb class for arbitrary html

[`class Image`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/image.md): Wandb class for images.

[`class Molecule`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/molecule.md): Wandb class for Molecular data

[`class Object3D`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/object3d.md): Wandb class for 3D point clouds.

[`class Plotly`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/plotly.md): Wandb class for plotly plots.

[`class Table`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/table.md): This is a table designed to display sets of records.

[`class Video`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/video.md): Wandb representation of video.

## Functions

[`agent(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/agent.md): Generic agent entrypoint, used for CLI or jupyter.

[`config(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/config.md): Config object

[`init(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/init.md): Start a new tracked run with `wandb.init()`.

[`join(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/join.md): Marks a run as finished, and finishes uploading all data.

[`log(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/log.md): Log a dict to the global run's history.

[`save(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/save.md): Ensure all files matching _glob\_str_ are synced to wandb with the policy specified.

[`setup(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/setup.md)

[`summary(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/summary.md): Summary tracks single values for each run. By default, summary is set to the

[`sweep(...)`](https://github.com/charlesfrye/docs-box/tree/04200c04fd5428a59ffc3441c64083036ef5542f/ref/sweep.md)

| Other Members |  |
| :--- | :--- |
|  \_\_version\_\_ |  \`'0.10.22'\` |

