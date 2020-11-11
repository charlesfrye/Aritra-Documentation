# _set_logger
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L37-L41)

`(log_object)`


Configure module logger.

| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|


**Hints**


**Returns**


**Example**

# _WandbInit
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L47-L440)





| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|


**Hints**


**Returns**


**Example**

# init
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L449-L608)

`( job_type: Optional[str] = None, dir=None, config: Union[Dict, str, None] = None, project: Optional[str] = None, entity: Optional[str] = None, reinit: bool = None, tags: Optional[Sequence] = None, group: Optional[str] = None, name: Optional[str] = None, notes: Optional[str] = None, magic: Union[dict, str, bool] = None, config_exclude_keys=None, config_include_keys=None, anonymous: Optional[str] = None, mode: Optional[str] = None, allow_val_change: Optional[bool] = None, resume: Optional[Union[bool, str]] = None, force: Optional[bool] = None, tensorboard=None, # alias for sync_tensorboard sync_tensorboard=None, monitor_gym=None, save_code=None, id=None, settings: Union[Settings, Dict[str, Any], None] = None, ) -> Union[Run, Dummy]`


Initialize W&B
Spawns a new process to start or resume a run locally and communicate with a
wandb server. Should be called before any calls to wandb.log.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|


**Hints**


**Returns**


**Example**

