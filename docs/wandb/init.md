description: Initialize W&B

robots: noindex

# wandb.init

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">

</table>

<a target="_blank" href="/home/aritra/anaconda3/envs/tf_docs/lib/python3.6/site-packages/wandb/sdk/wandb_init.py">View source</a>



Initialize W&B

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wandb.init(
    job_type: Optional[str] = None,
    dir=None,
    config: Union[Dict, str, None] = None,
    project: Optional[str] = None,
    entity: Optional[str] = None,
    reinit: bool = None,
    tags: Optional[Sequence] = None,
    group: Optional[str] = None,
    name: Optional[str] = None,
    notes: Optional[str] = None,
    magic: Union[dict, str, bool] = None,
    config_exclude_keys=None,
    config_include_keys=None,
    anonymous: Optional[str] = None,
    mode: Optional[str] = None,
    allow_val_change: Optional[bool] = None,
    resume: Optional[Union[bool, str]] = None,
    force: Optional[bool] = None,
    tensorboard=None,
    sync_tensorboard=None,
    monitor_gym=None,
    save_code=None,
    id=None,
    settings: Union[Settings, Dict[str, Any], None] = None
) -> Union[Run, Dummy, None]
</code></pre>



<!-- Placeholder for "Used in" -->
Spawns a new process to start or resume a run locally and communicate with a
wandb server. Should be called before any calls to wandb.log.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>
<tr class="alt">
<td colspan="2">
job_type (str, optional): The type of job running, defaults to 'train'
dir (str, optional): An absolute path to a directory where metadata will
be stored.
config (dict, argparse, or absl.flags, str, optional):
Sets the config parameters (typically hyperparameters) to store with the
run. See also wandb.config.
If dict, argparse or absl.flags: will load the key value pairs into
the runs config object.
If str: will look for a yaml file that includes config parameters and
load them into the run's config object.
project (str, optional): W&B Project.
entity (str, optional): W&B Entity.
reinit (bool, optional): Allow multiple calls to init in the same process.
tags (list, optional): A list of tags to apply to the run.
group (str, optional): A unique string shared by all runs in a given group.
name (str, optional): A display name for the run which does not have to be
unique.
notes (str, optional): A multiline string associated with the run.
magic (bool, dict, or str, optional): magic configuration as bool, dict,
json string, yaml filename.
config_exclude_keys (list, optional): string keys to exclude storing in W&B
when specifying config.
config_include_keys (list, optional): string keys to include storing in W&B
when specifying config.
anonymous (str, optional): Can be "allow", "must", or "never". Controls
whether anonymous logging is allowed.  Defaults to never.
mode (str, optional): Can be "online", "offline" or "disabled". Defaults to
online.
allow_val_change (bool, optional): allow config values to be changed after
setting. Defaults to true in jupyter and false otherwise.
resume (bool, str, optional): Sets the resuming behavior. Should be one of:
"allow", "must", "never", "auto" or None. Defaults to None.
Cases:
- "auto" (or True): automatically resume the previous run on the same machine.
if the previous run crashed, otherwise starts a new run.
- "allow": if id is set with init(id="UNIQUE_ID") or WANDB_RUN_ID="UNIQUE_ID"
and it is identical to a previous run, wandb will automatically resume the
run with the id. Otherwise wandb will start a new run.
- "never": if id is set with init(id="UNIQUE_ID") or WANDB_RUN_ID="UNIQUE_ID"
and it is identical to a previous run, wandb will crash.
- "must": if id is set with init(id="UNIQUE_ID") or WANDB_RUN_ID="UNIQUE_ID"
and it is identical to a previous run, wandb will automatically resume the
run with the id. Otherwise wandb will crash.
- None: never resumes - if a run has a duplicate run_id the previous run is
overwritten.
See https://docs.wandb.com/library/advanced/resuming for more detail.
force (bool, optional): If true, will cause script to crash if user can't or isn't
logged in to a wandb server.  If false, will cause script to run in offline
modes if user can't or isn't logged in to a wandb server. Defaults to false.
sync_tensorboard (bool, optional): Synchronize wandb logs from tensorboard or
tensorboardX and saves the relevant events file. Defaults to false.
</td>
</tr>
<tr>
<td>
`monitor_gym`
</td>
<td>
(bool, optional): automatically logs videos of environment when
using OpenAI Gym (see https://docs.wandb.com/library/integrations/openai-gym)
Defaults to false.
save_code (bool, optional): Save the entrypoint or jupyter session history
source code.
id (str, optional): A globally unique (per project) identifier for the run. This
is primarily used for resuming.
</td>
</tr>
</table>



#### Examples:

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



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`Exception`
</td>
<td>
if problem.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A `Run` object.
</td>
</tr>

</table>

