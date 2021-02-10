# Library

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

[`class Artifact`](https://github.com/ariG23498/Aritra-Documentation/tree/8583b5a558eb2bf679d5ca37d3ecf0c8a586bd5c/Platform/Library/Library/Artifact.md): An artifact object you can write files into, and pass to log\_artifact.

