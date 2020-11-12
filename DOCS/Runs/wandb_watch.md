# watch
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_watch.py#L12-L69)

`def watch(models, criterion=None, log="gradients", log_freq=1000, idx=None)`



Hooks into the torch model to collect gradients and the topology.  Should be extended
to accept arbitrary ML models.

| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|models|(torch.Module)|The model to hook, can be a tuple|
|criterion|(torch.F)|An optional loss value being optimized|
|log|(str)|One of "gradients", "parameters", "all", or None|
|log_freq|(int)|log gradients and parameters every N batches|
|idx|(int)|an index to be used when calling wandb.watch on multiple models|






**Reutrns**

`wandb.Graph` The graph object that will populate after the first backward pass



# unwatch
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_watch.py#L70-L87)

`def unwatch(models=None)`


Remove pytorch gradient and parameter hooks.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|models|(list)|Optional list of pytorch models that have had watch called on them|









