# watch
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_watch.py#L12-L68)

`def watch(models, criterion=None, log="gradients", log_freq=1000, idx=None):`

Hooks into the torch model to collect gradients and the topology.  Should be extended
to accept arbitrary ML models.







**Reutrns**

`wandb.Graph` The graph object that will populate after the first backward pass




# unwatch
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_watch.py#L70-L86)

`def unwatch(models=None):`

Remove pytorch gradient and parameter hooks.












