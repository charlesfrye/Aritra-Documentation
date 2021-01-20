# Module: wandb

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/__init__.py)



Wandb is a library to help track machine learning experiments.


For more information on wandb see https://docs.wandb.com.

The most commonly used functions/objects are:
- wandb.init — initialize a new run at the top of your training script
- wandb.config — track hyperparameters
- wandb.log — log metrics over time within your training loop
- wandb.save — save files in association with your run, like model weights
- wandb.restore — restore the state of your code when you ran a given run

For examples usage, see github.com/wandb/examples

## Classes

[`class Api`](./wandb/Api.md): Used for querying the wandb server.

[`class Audio`](./wandb/Audio.md): Wandb class for audio clips.

[`class Graph`](./wandb/Graph.md): Wandb class for graphs

[`class Histogram`](./wandb/Histogram.md): wandb class for histograms

[`class Html`](./wandb/Html.md): Wandb class for arbitrary html

[`class Image`](./wandb/Image.md): Wandb class for images.

[`class Molecule`](./wandb/Molecule.md): Wandb class for Molecular data

[`class Object3D`](./wandb/Object3D.md): Wandb class for 3D point clouds.

[`class Plotly`](./wandb/Plotly.md): Wandb class for plotly plots.

[`class Table`](./wandb/Table.md): This is a table designed to display sets of records.

[`class Video`](./wandb/Video.md): Wandb representation of video.

## Functions

[`agent(...)`](./wandb/agent.md): Generic agent entrypoint, used for CLI or jupyter.

[`config(...)`](./wandb/config.md): Config object

[`init(...)`](./wandb/init.md): Initialize W&B.

[`join(...)`](./wandb/join.md)

[`log(...)`](./wandb/log.md): Log a dict to the global run's history.

[`save(...)`](./wandb/save.md): Ensure all files matching *glob_str* are synced to wandb with the policy specified.

[`setup(...)`](./wandb/setup.md)

[`summary(...)`](./wandb/summary.md): Summary tracks single values for each run. By default, summary is set to the

[`sweep(...)`](./wandb/sweep.md)



<!-- Tabular view -->
 <table>
<tr><th>Other Members</th></tr>
<tr>
<td>
__version__<a id="__version__"></a>
</td>
<td>
`'0.10.14'`
</td>
</tr>
</table>

