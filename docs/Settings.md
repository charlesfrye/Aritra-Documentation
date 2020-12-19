This module configures settings for wandb runs.

Order of loading settings: (differs from priority)
    defaults
    environment
    wandb.setup(settings=)
    system_config
    workspace_config
    wandb.init(settings=)
    network_org
    network_entity
    network_project

Priority of settings:  See "source" variable.

When override is used, it has priority over non-override settings

Override priorities are in the reverse order of non-override settings
# Settings
`class Settings(object):`

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_settings.py#L187-#L951)

****
    
Settings Constructor

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| entity |  | personal user or team to use for Run. |
| project |  | project name for the Run. |
**Raises**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| Exception |  | if problem. |
## _path_convert_part
`def _path_convert_part(self, path_part, format_dict): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_settings.py#L610-#L619)

****
    
convert slashes, expand ~ and other macros.
    
## _path_convert
`def _path_convert(self, *path): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_settings.py#L621-#L645)

****
    
convert slashes, expand ~ and other macros.
    
## __copy__
`def __copy__(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_settings.py#L656-#L660)

****
    
Copy (note that the copied object will not be frozen).
    
## _infer_settings_from_env
`def _infer_settings_from_env(self): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_settings.py#L718-#L773)

****
    
Modify settings based on environment (for runs and cli).
    
## _infer_run_settings_from_env
`def _infer_run_settings_from_env(self, _logger=None): `

[![Badge](https://img.shields.io/badge/SOURCE-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_settings.py#L775-#L790)

****
    
Modify settings based on environment (for runs only).
    
