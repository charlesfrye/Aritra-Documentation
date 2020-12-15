

``

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_watch.py#L0-#L0)
****
    
watch.
    
# watch

`def watch(models, criterion=None, log="gradients", log_freq=1000, idx=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_watch.py#L18-#L94)
****
    
Hooks into the torch model to collect gradients and the topology.  Should be extended
to accept arbitrary ML models.

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| models | (torch.Module) | The model to hook, can be a tuple |
| criterion | (torch.F) | An optional loss value being optimized |
| log | (str) | One of "gradients", "parameters", "all", or None |
| log_freq | (int) | log gradients and parameters every N batches |
| idx | (int) | an index to be used when calling wandb.watch on multiple models |
**Returns**
    
`wandb.Graph` The graph object that will populate after the first backward pass
    
# unwatch

`def unwatch(models=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_watch.py#L97-#L113)
****
    
Remove pytorch gradient and parameter hooks.

    
**Args**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| models | (list) | Optional list of pytorch models that have had watch called on them |
