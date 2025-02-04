# public-api

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/__init__.py)




Use the Public API to export or update data that you have saved to W&B.

Before using this API, you'll want to log data from your script — check the [Quickstart](../quickstart.md) for more details.

**Use Cases for the Public API**

* **Export Data**: Pull down a dataframe for custom analysis in a Jupyter Notebook. Once you have explored the data, you can sync your findings by creating a new analysis run and logging results, for example: `wandb.init(job_type="analysis")`
* **Update Existing Runs**: You can update the data logged in association with a W&B run. For example, you might want to update the config of a set of runs to include additional information, like the architecture or a hyperparameter that wasn't originally logged.

See the [Generated Reference Docs](../ref/public-api/) for details on available functions.

## Classes

[`class Api`](./api.md): Used for querying the wandb server.

[`class Artifact`](./artifact.md): An artifact that has been logged, including all its attributes, links to the runs

[`class File`](./file.md): File is a class associated with a file saved by wandb.

[`class Files`](./files.md): Files is an iterable collection of `File` objects.

[`class Project`](./project.md): A project is a namespace for runs

[`class Projects`](./projects.md): An iterable collection of `Project` objects.

[`class Run`](./run.md): A single run associated with an entity and project.

[`class Runs`](./runs.md): An iterable collection of runs associated with a project and optional filter.

[`class Sweep`](./sweep.md): A set of runs associated with a sweep

