# init
`def init( job_type: Optional[str] = None, dir=None, config: Union[Dict, str, None] = None, project: Optional[str] = None, entity: Optional[str] = None, reinit: bool = None, tags: Optional[Sequence] = None, group: Optional[str] = None, name: Optional[str] = None, notes: Optional[str] = None, magic: Union[dict, str, bool] = None, config_exclude_keys=None, config_include_keys=None, anonymous: Optional[str] = None, mode: Optional[str] = None, allow_val_change: Optional[bool] = None, resume: Optional[Union[bool, str]] = None, force: Optional[bool] = None, tensorboard=None, # alias for sync_tensorboard sync_tensorboard=None, monitor_gym=None, save_code=None, id=None, settings: Union[Settings, Dict[str, Any], None] = None, ) -> Union[Run, Dummy]: Union[Run, Dummy]`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_init.py#L468-#L625)

****
    
Initialize W&B
Spawns a new process to start or resume a run locally and communicate with a
wandb server. Should be called before any calls to wandb.log.

    
**Arguments**
    
config (dict, argparse, or absl.flags, str, optional):
    Sets the config parameters (typically hyperparameters) to store with the
    run. See also wandb.config.

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| job_type | (str, optional) | The type of job running, defaults to 'train' |
| dir | (str, optional) | An absolute path to a directory where metadata will be stored. |
| flags |  | will load the key value pairs into the runs config object. If str: will look for a yaml file that includes config parameters and load them into the run's config object. |
| project | (str, optional) | W&B Project. |
| entity | (str, optional) | W&B Entity. |
| reinit | (bool, optional) | Allow multiple calls to init in the same process. |
| tags | (list, optional) | A list of tags to apply to the run. |
| group | (str, optional) | A unique string shared by all runs in a given group. |
| name | (str, optional) | A display name for the run which does not have to be unique. |
| notes | (str, optional) | A multiline string associated with the run. |
| magic | (bool, dict, or str, optional) | magic configuration as bool, dict, json string, yaml filename. |
| config_exclude_keys | (list, optional) | string keys to exclude storing in W&B when specifying config. |
| config_include_keys | (list, optional) | string keys to include storing in W&B when specifying config. |
| anonymous | (str, optional) | Can be "allow", "must", or "never". Controls whether anonymous logging is allowed. Defaults to never. |
| mode | (str, optional) | Can be "online", "offline" or "disabled". Defaults to online. |
| allow_val_change | (bool, optional) | allow config values to be changed after setting. Defaults to true in jupyter and false otherwise. |
| resume | (bool, str, optional) | Sets the resuming behavior. Should be one of: "allow", "must", "never", "auto" or None. Defaults to None. Cases: - "auto" (or True): automatically resume the previous run on the same machine. if the previous run crashed, otherwise starts a new run. - "allow": if id is set with init(id="UNIQUE_ID") or WANDB_RUN_ID="UNIQUE_ID" and it is identical to a previous run, wandb will automatically resume the run with the id. Otherwise wandb will start a new run. - "never": if id is set with init(id="UNIQUE_ID") or WANDB_RUN_ID="UNIQUE_ID" and it is identical to a previous run, wandb will crash. - "must": if id is set with init(id="UNIQUE_ID") or WANDB_RUN_ID="UNIQUE_ID" and it is identical to a previous run, wandb will automatically resume the run with the id. Otherwise wandb will crash. - None: never resumes - if a run has a duplicate run_id the previous run is overwritten. See https://docs.wandb.com/library/advanced/resuming for more detail. |
| force | (bool, optional) | If true, will cause script to crash if user can't or isn't logged in to a wandb server. If false, will cause script to run in offline modes if user can't or isn't logged in to a wandb server. Defaults to false. |
| sync_tensorboard | (bool, optional) | Synchronize wandb logs from tensorboard or tensorboardX and saves the relevant events file. Defaults to false. |
| monitor_gym |  | (bool, optional): automatically logs videos of environment when using OpenAI Gym (see https://docs.wandb.com/library/integrations/openai-gym) Defaults to false. |
| save_code | (bool, optional) | Save the entrypoint or jupyter session history source code. |
| id | (str, optional) | A globally unique (per project) identifier for the run. This is primarily used for resuming. |
**Examples**
    
Basic usage
```
wandb.init()
```

Launch multiple runs from the same script
```
for x in range(10):
    with wandb.init(project="my-projo") as run:
        for y in range(100):
            run.log({"metric": x+y})
```

    
**Raises**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| Exception |  | if problem. |
**Returns**
    
A `Run` object.
    
## log
`def log(self, data, step=None, commit=None, sync=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L731-#L864)

****
    
Log a dict to the global run's history.

`wandb.log` can be used to log everything from scalars to histograms, media
and matplotlib plots.

The most basic usage is `wandb.log({'train-loss': 0.5, 'accuracy': 0.9})`.
This will save a history row associated with the run with train-loss=0.5
and `accuracy=0.9`. The history values can be plotted on app.wandb.ai or
on a local server. The history values can also be downloaded through
the wandb API.

Logging a value will update the summary values for any metrics logged.
The summary values will appear in the run table at app.wandb.ai or
a local server. If a summary value is manually set with for example
`wandb.run.summary["accuracy"] = 0.9` `wandb.log` will no longer automatically
update the run's accuracy.

Logging values don't have to be scalars. Logging any wandb object is supported.
For example `wandb.log({"example": wandb.Image("myimage.jpg")})` will log an
example image which will be displayed nicely in the wandb UI. See
https://docs.wandb.com/library/reference/data_types for all of the different
supported types.

Logging nested metrics is encouraged and is supported in the wandb API, so
you could log multiple accuracy values with `wandb.log({'dataset-1':
{'acc': 0.9, 'loss': 0.3} ,'dataset-2': {'acc': 0.8, 'loss': 0.2}})`
and the metrics will be organized in the wandb UI.

W&B keeps track of a global step so logging related metrics together is
encouraged, so by default each time wandb.log is called a global step
is incremented. If it's inconvenient to log related metrics together
calling `wandb.log({'train-loss': 0.5, commit=False})` and then
`wandb.log({'accuracy': 0.9})` is equivalent to calling
`wandb.log({'train-loss': 0.5, 'accuracy': 0.9})`

wandb.log is not intended to be called more than a few times per second.
If you want to log more frequently than that it's better to aggregate
the data on the client side or you may get degraded performance.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| row | (dict, optional) | A dict of serializable python objects i.e `str`, `ints`, `floats`, `Tensors`, `dicts`, or `wandb.data_types`. |
| commit | (boolean, optional) | Save the metrics dict to the wandb server and increment the step. If false `wandb.log` just updates the current metrics dict with the row argument and metrics won't be saved until `wandb.log` is called with `commit=True`. |
| step | (integer, optional) | The global step in processing. This persists any non-committed earlier steps but defaults to not committing the specified step. |
| sync | (boolean, True) | This argument is deprecated and currently doesn't change the behaviour of `wandb.log`. |
**Examples**
    
Basic usage
```python
wandb.log({'accuracy': 0.9, 'epoch': 5})
```

Incremental logging
```python
wandb.log({'loss': 0.2}, commit=False)
# Somewhere else when I'm ready to report this step:
wandb.log({'accuracy': 0.8})
```

Histogram
```python
wandb.log({"gradients": wandb.Histogram(numpy_array_or_sequence)})
```

Image
```python
wandb.log({"examples": [wandb.Image(numpy_array_or_pil, caption="Label")]})
```

Video
```python
wandb.log({"video": wandb.Video(numpy_array_or_video_path, fps=4,
    format="gif")})
```

Matplotlib Plot
```python
wandb.log({"chart": plt})
```

PR Curve
```python
wandb.log({'pr': wandb.plots.precision_recall(y_test, y_probas, labels)})
```

3D Object
```python
wandb.log({"generated_samples":
[wandb.Object3D(open("sample.obj")),
    wandb.Object3D(open("sample.gltf")),
    wandb.Object3D(open("sample.glb"))]})
```

For more examples, see https://docs.wandb.com/library/log

    
**Raises**
    
wandb.Error - if called before `wandb.init`
ValueError - if invalid data is passed
    
# watch
`def watch(models, criterion=None, log="gradients", log_freq=1000, idx=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_watch.py#L18-#L94)

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
    
save.
# login
`def login(anonymous=None, key=None, relogin=None, host=None, force=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_login.py#L22-#L42)

****
    
Log in to W&B.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| anonymous | (string, optional) | Can be "must", "allow", or "never". If set to "must" we'll always login anonymously, if set to "allow" we'll only create an anonymous user if the user isn't already logged in. |
| key | (string, optional) | authentication key. |
| relogin | (bool, optional) | If true, will re-prompt for API key. |
| host | (string, optional) | The host to connect to. |
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| bool |  | if key is configured |
**Raises**
    
UsageError - if api_key can not configured and no tty
    
## finish
`def finish(self, exit_code=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L961-#L973)

****
    
Marks a run as finished, and finishes uploading all data.  This is
used when creating multiple runs in the same process.  We automatically
call this method when your script exits.
    
