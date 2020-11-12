# doc

## \_set\_logger

[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L37-L41)

`def _set_logger(log_object)`

Configure module logger.

**Hints**

**Returns**

**Example**

## \_WandbInit

[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L47-L441)

**Hints**

**Returns**

**Example**

## init

[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/Folder/demo.py#L450-L609)

`def init( job_type: Optional[str] = None, dir=None, config: Union[Dict, str, None] = None, project: Optional[str] = None, entity: Optional[str] = None, reinit: bool = None, tags: Optional[Sequence] = None, group: Optional[str] = None, name: Optional[str] = None, notes: Optional[str] = None, magic: Union[dict, str, bool] = None, config_exclude_keys=None, config_include_keys=None, anonymous: Optional[str] = None, mode: Optional[str] = None, allow_val_change: Optional[bool] = None, resume: Optional[Union[bool, str]] = None, force: Optional[bool] = None, tensorboard=None, # alias for sync_tensorboard sync_tensorboard=None, monitor_gym=None, save_code=None, id=None, settings: Union[Settings, Dict[str, Any], None] = None, ) -> Union[Run, Dummy]`

Initialize W&B Spawns a new process to start or resume a run locally and communicate with a wandb server. Should be called before any calls to wandb.log.

<table>
  <thead>
    <tr>
      <th style="text-align:center"><b>Arguments</b>
      </th>
      <th style="text-align:center"><b>Datatype</b>
      </th>
      <th style="text-align:left"><b>Description</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center">job_type</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">The type of job running, defaults to &apos;train&apos;</td>
    </tr>
    <tr>
      <td style="text-align:center">dir</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">An absolute path to a directory where metadata will be stored.</td>
    </tr>
    <tr>
      <td style="text-align:center">flags</td>
      <td style="text-align:center"></td>
      <td style="text-align:left">will load the key value pairs into the runs config object. If str: will
        look for a yaml file that includes config parameters and load them into
        the run&apos;s config object.</td>
    </tr>
    <tr>
      <td style="text-align:center">project</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">W&amp;B Project.</td>
    </tr>
    <tr>
      <td style="text-align:center">entity</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">W&amp;B Entity.</td>
    </tr>
    <tr>
      <td style="text-align:center">reinit</td>
      <td style="text-align:center">(bool, optional)</td>
      <td style="text-align:left">Allow multiple calls to init in the same process.</td>
    </tr>
    <tr>
      <td style="text-align:center">tags</td>
      <td style="text-align:center">(list, optional)</td>
      <td style="text-align:left">A list of tags to apply to the run.</td>
    </tr>
    <tr>
      <td style="text-align:center">group</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">A unique string shared by all runs in a given group.</td>
    </tr>
    <tr>
      <td style="text-align:center">name</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">A display name for the run which does not have to be unique.</td>
    </tr>
    <tr>
      <td style="text-align:center">notes</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">A multiline string associated with the run.</td>
    </tr>
    <tr>
      <td style="text-align:center">magic</td>
      <td style="text-align:center">(bool, dict, or str, optional)</td>
      <td style="text-align:left">magic configuration as bool, dict, json string, yaml filename.</td>
    </tr>
    <tr>
      <td style="text-align:center">config_exclude_keys</td>
      <td style="text-align:center">(list, optional)</td>
      <td style="text-align:left">string keys to exclude storing in W&amp;B when specifying config.</td>
    </tr>
    <tr>
      <td style="text-align:center">config_include_keys</td>
      <td style="text-align:center">(list, optional)</td>
      <td style="text-align:left">string keys to include storing in W&amp;B when specifying config.</td>
    </tr>
    <tr>
      <td style="text-align:center">anonymous</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">Can be &quot;allow&quot;, &quot;must&quot;, or &quot;never&quot;. Controls
        whether anonymous logging is allowed. Defaults to never.</td>
    </tr>
    <tr>
      <td style="text-align:center">mode</td>
      <td style="text-align:center">(str, optional)</td>
      <td style="text-align:left">Can be &quot;online&quot;, &quot;offline&quot; or &quot;disabled&quot;.
        Defaults to online.</td>
    </tr>
    <tr>
      <td style="text-align:center">allow_val_change</td>
      <td style="text-align:center">(bool, optional)</td>
      <td style="text-align:left">allow config values to be changed after setting. Defaults to true in jupyter
        and false otherwise.</td>
    </tr>
    <tr>
      <td style="text-align:center">resume</td>
      <td style="text-align:center">(bool, str, optional)</td>
      <td style="text-align:left">
        <p>Sets the resuming behavior. Should be one of: &quot;allow&quot;, &quot;must&quot;,
          &quot;never&quot;, &quot;auto&quot; or None. Defaults to None. Cases:</p>
        <ul>
          <li>&quot;auto&quot; (or True): automatically resume the previous run on the
            same machine. if the previous run crashed, otherwise starts a new run.</li>
          <li>&quot;allow&quot;: if id is set with init(id=&quot;UNIQUE_ID&quot;) or
            WANDB_RUN_ID=&quot;UNIQUE_ID&quot; and it is identical to a previous run,
            wandb will automatically resume the run with the id. Otherwise wandb will
            start a new run.</li>
          <li>&quot;never&quot;: if id is set with init(id=&quot;UNIQUE_ID&quot;) or
            WANDB_RUN_ID=&quot;UNIQUE_ID&quot; and it is identical to a previous run,
            wandb will crash.</li>
          <li>&quot;must&quot;: if id is set with init(id=&quot;UNIQUE_ID&quot;) or
            WANDB_RUN_ID=&quot;UNIQUE_ID&quot; and it is identical to a previous run,
            wandb will automatically resume the run with the id. Otherwise wandb will
            crash.</li>
          <li>None: never resumes</li>
          <li>if a run has a duplicate run_id the previous run is overwritten. See
            <a
            href="https://docs.wandb.com/library/advanced/resuming">https://docs.wandb.com/library/advanced/resuming</a>for more detail.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:center">force</td>
      <td style="text-align:center">(bool, optional)</td>
      <td style="text-align:left">if tru will cause something.</td>
    </tr>
  </tbody>
</table>

|  |
| :--- |


**Hints**

**Returns**

**Example**

