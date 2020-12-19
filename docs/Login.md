Log in to Weights & Biases, authenticating your machine to log data to your
account.
# login
`def login(anonymous=None, key=None, relogin=None, host=None, force=None): `

[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=plastic&logo=github)](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_login.py#L22-#L42)

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
    
