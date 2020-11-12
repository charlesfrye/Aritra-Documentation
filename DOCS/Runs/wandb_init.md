# _set_logger
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L37-L41)

`def _set_logger(log_object)`


Configure module logger.










# _WandbInit
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L47-L438)














## _WandbInit.setup
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L59-L156)

`def _WandbInit.setup(self, kwargs)`



Complete setup for wandb.init(). This includes parsing all arguments, 
applying them with settings and enabling logging.











## _WandbInit._enable_logging
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L164-L198)

`def _WandbInit._enable_logging(self, log_fname, run_id=None)`



Enable logging to the global debug log.  This adds a run_id to the log,
in case of muliple processes on the same machine.
Currently there is no way to disable logging after it's enabled.











## _WandbInit._jupyter_teardown
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L229-L243)

`def _WandbInit._jupyter_teardown(self)`


Teardown hooks and display saving, called with wandb.finish










## _WandbInit._jupyter_setup
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L244-L267)

`def _WandbInit._jupyter_setup(self, settings)`


Add magic, hooks, and session history saving










## _WandbInit._log_setup
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L268-L302)

`def _WandbInit._log_setup(self, settings)`


Set up logging from settings.










# init
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_init.py#L447-L605)

`def init( job_type: Optional[str] = None, dir=None, config: Union[Dict, str, None] = None, project: Optional[str] = None, entity: Optional[str] = None, reinit: bool = None, tags: Optional[Sequence] = None, group: Optional[str] = None, name: Optional[str] = None, notes: Optional[str] = None, magic: Union[dict, str, bool] = None, config_exclude_keys=None, config_include_keys=None, anonymous: Optional[str] = None, mode: Optional[str] = None, allow_val_change: Optional[bool] = None, resume: Optional[Union[bool, str]] = None, force: Optional[bool] = None, tensorboard=None, # alias for sync_tensorboard sync_tensorboard=None, monitor_gym=None, save_code=None, id=None, settings: Union[Settings, Dict[str, Any], None] = None, ) -> Union[Run, Dummy]`


Initialize W&B
Spawns a new process to start or resume a run locally and communicate with a
wandb server. Should be called before any calls to wandb.log.






{% hint style="info" %}
:if problem.
{% endhint %}

**Reutrns**

A `Run` object.


**Example**

Basic usage
```
wandb.init()
```

Launch multiple runs from the same script
```
for x in range(10):
    with wandb.init(project="my-projo") as run:
        for y in range(100):
```

