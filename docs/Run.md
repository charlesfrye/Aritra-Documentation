# Run

`class Run(object):`

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L134-#L1812)
****
    
The run object corresponds to a single execution of your script,
typically this is an ML experiment. Create a run with wandb.init().

In distributed training, use wandb.init() to create a run for each process,
and set the group argument to organize runs into a larger experiment.

Currently there is a parallel Run object in the wandb.Api. Eventually these
two objects will be merged.

    
**Attributes**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| history | (`History`) | Time series values, created with wandb.log(). History can contain scalar values, rich media, or even custom plots across multiple steps. |
| summary | (`Summary`) | Single values set for each wandb.log() key. By default, summary is set to the last value logged. You can manually set summary to the best value, like max accuracy, instead of the final value. |
## _telemetry_get_framework

`def _telemetry_get_framework(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L264-#L288)
****
    
Get telemetry data for internal config structure.
    
## _make_proto_run

`def _make_proto_run(self, run): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L306-#L326)
****
    
Populate protocol buffer RunData for interface/interface.
    
## dir

`def dir(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L335-#L341)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | The directory where all of the files associated with the run are placed. |
## config

`def config(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L343-#L350)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (`Config`) | A config object (similar to a nested dict) of key value pairs associated with the hyperparameters of the run. |
## name

`def name(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L356-#L367)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | the display name of the run. It does not need to be unique and ideally is descriptive. |
## notes

`def notes(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L375-#L385)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | notes associated with the run. Notes can be a multiline string and can also use markdown and latex equations inside $$ like $\{x} |
## tags

`def tags(self) -> Optional[Tuple]: Optional[Tuple]`

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L393-#L402)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (Tuple[str]) | tags associated with the run |
## id

`def id(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L410-#L416)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | the run_id associated with the run |
## sweep_id

`def sweep_id(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L418-#L426)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str, optional) | the sweep id associated with the run or None |
## path

`def path(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L428-#L438)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | the path to the run [entity]/[project]/[run_id] |
## start_time

`def start_time(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L440-#L449)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (int) | the unix time stamp in seconds when the run started |
## starting_step

`def starting_step(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L451-#L460)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (int) | the first step of the run |
## resumed

`def resumed(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L462-#L471)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (bool) | whether or not the run was resumed |
## step

`def step(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L473-#L482)
****
    
Every time you call wandb.log() it will by default increment the step
counter.

    
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (int) | step counter |
## mode

`def mode(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L488-#L491)
****
    
For compatibility with 0.9.x and earlier, deprecate eventually.
    
## group

`def group(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L501-#L515)
****
    
Setting a group helps the W&B UI organize runs in a sensible way.

If you are doing a distributed training you should give all of the
runs in the training the same group.
    
****
    
If you are doing crossvalidation you should give all the crossvalidation
    folds the same group.

    
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | name of W&B group associated with run. |
## project

`def project(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L522-#L528)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | name of W&B project associated with run. |
## get_url

`def get_url(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L530-#L538)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str, optional) | url for the W&B run or None if the run is offline |
## get_project_url

`def get_project_url(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L540-#L549)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str, optional) | url for the W&B project associated with the run or None if the run is offline. |
## get_sweep_url

`def get_sweep_url(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L551-#L560)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str, optional) | url for the sweep associated with the run or None if there is no associated sweep or the run is offline. |
## url

`def url(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L562-#L568)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | name of W&B url associated with run. |
## entity

`def entity(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L570-#L577)
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | name of W&B entity associated with run. Entity is either a user name or an organization name. |
## _add_singleton

`def _add_singleton(self, type, key, value): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L702-#L727)
****
    
Stores a singleton item to wandb config.

A singleton in this context is a piece of data that is continually
logged with the same value in each history step, but represented
as a single item in the config.

We do this to avoid filling up history with a lot of repeated uneccessary data

Add singleton can be called many times in one run and it will only be
updated when the value changes. The last value logged will be the one
persisted to the server
    
## log

`def log(self, data, step=None, commit=None, sync=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L729-#L862)
****
    
Log a dict to the global run's history.

wandb.log can be used to log everything from scalars to histograms, media
and matplotlib plots.

The most basic usage is wandb.log({'train-loss': 0.5, 'accuracy': 0.9}).
This will save a history row associated with the run with train-loss=0.5
and accuracy=0.9. The history values can be plotted on app.wandb.ai or
on a local server. The history values can also be downloaded through
the wandb API.

Logging a value will update the summary values for any metrics logged.
The summary values will appear in the run table at app.wandb.ai or
a local server. If a summary value is manually set with for example
wandb.run.summary["accuracy"] = 0.9 wandb.log will no longer automatically
update the run's accuracy.

Logging values don't have to be scalars. Logging any wandb object is supported.
For example wandb.log({"example": wandb.Image("myimage.jpg")}) will log an
example image which will be displayed nicely in the wandb UI. See
https://docs.wandb.com/library/reference/data_types for all of the different
supported types.

Logging nested metrics is encouraged and is supported in the wandb API, so
you could log multiple accuracy values with wandb.log({'dataset-1':
{'acc': 0.9, 'loss': 0.3} ,'dataset-2': {'acc': 0.8, 'loss': 0.2}})
and the metrics will be organized in the wandb UI.

W&B keeps track of a global step so logging related metrics together is
encouraged, so by default each time wandb.log is called a global step
is incremented. If it's inconvenient to log related metrics together
calling wandb.log({'train-loss': 0.5, commit=False}) and then
wandb.log({'accuracy': 0.9}) is equivalent to calling
wandb.log({'train-loss': 0.5, 'accuracy': 0.9})

wandb.log is not intended to be called more than a few times per second.
If you want to log more frequently than that it's better to aggregate
the data on the client side or you may get degraded performance.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| row | (dict, optional) | A dict of serializable python objects i.e str, ints, floats, Tensors, dicts, or wandb.data_types |
| commit | (boolean, optional) | Save the metrics dict to the wandb server and increment the step. If false wandb.log just updates the current metrics dict with the row argument and metrics won't be saved until wandb.log is called with commit=True. |
| step | (integer, optional) | The global step in processing. This persists any non-committed earlier steps but defaults to not committing the specified step. |
| sync | (boolean, True) | This argument is deprecated and currently doesn't change the behaviour of wandb.log |
**Examples**
    
Basic usage
```
```

Incremental logging
```
# Somewhere else when I'm ready to report this step:
```

Histogram
```
```

Image
```
```

Video
```
```

Matplotlib Plot
```
```

PR Curve
```
```

3D Object
```
wandb.log({"generated_samples":
[wandb.Object3D(open("sample.obj")),
    wandb.Object3D(open("sample.gltf")),
    wandb.Object3D(open("sample.glb"))]})
```

For more examples, see https://docs.wandb.com/library/log

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  |  | 0.9, 'epoch': 5}) |
|  |  | 0.2}, commit=False) |
|  |  | 0.8}) |
|  |  | wandb.Histogram(numpy_array_or_sequence)}) |
|  |  | [wandb.Image(numpy_array_or_pil, caption="Label")]}) |
|  |  | wandb.Video(numpy_array_or_video_path, fps=4, format="gif")}) |
|  |  | plt}) |
|  |  | wandb.plots.precision_recall(y_test, y_probas, labels)}) |
**Raises**
    
wandb.Error - if called before wandb.init
ValueError - if invalid data is passed
    
## save

`def save( self, glob_str: Optional[str] = None, base_path: Optional[str] = None, policy: str = "live", ): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L864-#L948)
****
    
Ensure all files matching *glob_str* are synced to wandb with the policy specified.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| glob_str | (string) | a relative or absolute path to a unix glob or regular path. If this isn't specified the method is a noop. |
| base_path | (string) | the base path to run the glob relative to |
| policy | (string) | on of "live", "now", or "end" live: upload the file as it changes, overwriting the previous version now: upload the file once now end: only upload file when the run ends |
## finish

`def finish(self, exit_code=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L959-#L972)
****
    
Marks a run as finished, and finishes uploading all data.  This is
used when creating multiple runs in the same process.  We automatically
call this method when your script exits.
    
## join

`def join(self): self.stop() self._thread.join() class Run(object): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L974-#L976)
****
    
Deprecated alias for finish() - please use finish
    
## plot_table

`def plot_table(self, vega_spec_name, data_table, fields, string_fields=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L978-#L994)
****
    
Creates a custom plot on a table.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| vega_spec_name |  | the name of the spec for the plot |
| table_key |  | the key used to log the data table |
| data_table |  | a wandb.Table object containing the data to be used on the visualization |
| fields |  | a dict mapping from table keys to fields that the custom visualization needs |
| string_fields |  | a dict that provides values for any string constants the custom visualization needs |
## _get_sweep_url

`def _get_sweep_url(self): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L1046-#L1067)
****
    
Generate a url for a sweep.

    
**Returns**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
|  | (str) | url if the run is part of a sweep |
|  | (None) | if the run is not part of the sweep |
## use_artifact

`def use_artifact(self, artifact_or_name, type=None, aliases=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L1638-#L1688)
****
    
Declare an artifact as an input to a run, call `download` or `file` on         the returned object to get the contents locally.

    
**Arguments**
    
May be prefixed with entity/project. Valid names
    can be in the following forms:
        name:version
        name:alias
        digest
    You can also pass an Artifact object created by calling `wandb.Artifact`
    
| **Filed** | **Type** | **Description** |
|--|--|--|
| artifact_or_name | (str or Artifact) | An artifact name. |
| type | (str, optional) | The type of artifact to use. |
| aliases | (list, optional) | Aliases to apply to this artifact |
**Returns**
    
A #Artifact object.
    
## log_artifact

`def log_artifact(self, artifact_or_path, name=None, type=None, aliases=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L1691-#L1744)
****
    
Declare an artifact as output of a run.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| artifact_or_path | (str or Artifact) | A path to the contents of this artifact, can be in the following forms: /local/directory /local/directory/file.txt s3://bucket/path You can also pass an Artifact object created by calling `wandb.Artifact`. |
| name | (str, optional) | An artifact name. May be prefixed with entity/project. Valid names can be in the following forms: name:version name:alias digest This will default to the basename of the path prepended with the current run id if not specified. |
| type | (str) | The type of artifact to log, examples include "dataset", "model" |
| aliases | (list, optional) | Aliases to apply to this artifact, defaults to ["latest"] |
**Returns**
    
A `Artifact` object.
    
## alert

`def alert(self, title, text, level=None, wait_duration=None): `

[SOURCE](https://github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L1770-#L1799)
****
    
Launch an alert with the given title and text.

    
**Arguments**
    

    
| **Filed** | **Type** | **Description** |
|--|--|--|
| title | (str) | The title of the alert, must be less than 64 characters long |
| text | (str) | The text body of the alert |
| level | (str or wandb.AlertLevel, optional) | The alert level to use, either: "INFO", "WARN", or "ERROR" |
| wait_duration | (int, float, or timedelta, optional) | The time to wait (in seconds) before sending another alert with this title |
