# Public API

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

[`class Api`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Api.md): Used for querying the wandb server.

[`class Artifact`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Artifact.md)

[`class File`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/File.md): File is a class associated with a file saved by wandb.

[`class Files`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Files.md): Files is an iterable collection of `File` objects.

[`class Project`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Project.md): A project is a namespace for runs

[`class Projects`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Projects.md): An iterable collection of `Project` objects.

[`class Run`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Run.md): A single run associated with an entity and project.

[`class Runs`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Runs.md): An iterable collection of runs associated with a project and optional filter.

[`class Sweep`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Public%20API/Public%20API/Sweep.md): A set of runs associated with a sweep

