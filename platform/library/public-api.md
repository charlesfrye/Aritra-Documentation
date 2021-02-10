# public-api

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/__init__.py)




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

[`class Api`](./public-api/Api.md): Used for querying the wandb server.

[`class Artifact`](./public-api/Artifact.md)

[`class File`](./public-api/File.md): File is a class associated with a file saved by wandb.

[`class Files`](./public-api/Files.md): Files is an iterable collection of `File` objects.

[`class Project`](./public-api/Project.md): A project is a namespace for runs

[`class Projects`](./public-api/Projects.md): An iterable collection of `Project` objects.

[`class Run`](./public-api/Run.md): A single run associated with an entity and project.

[`class Runs`](./public-api/Runs.md): An iterable collection of runs associated with a project and optional filter.

[`class Sweep`](./public-api/Sweep.md): A set of runs associated with a sweep

