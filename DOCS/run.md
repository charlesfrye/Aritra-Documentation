# RunStatusChecker
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L97-L134)

`class RunStatusChecker(object)`


Periodically polls the background process for relevant updates.

For now, we just use this to figure out if the user has requested a stop.











# Run
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L136-L1705)

`class Run(object)`


Defines a wandb run, which typically corresponds to an ML experiment.

A run is created with wandb.init()

If you do distributed training, each process should be in its own run and
the group should be set in wandb.init to link the runs together.

There is a parallel Run object in wandb's API, eventually it will be merged
with this object.




| **Attributes** | **Datatype** | **Description** |
|:--:|:--:|:--|
|summary|(Summary)|summary statistics collected as training code runs.|
|history|(History)|history of data logged with wandb.log associated with run.|







## Run._telemetry_get_framework
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L263-L288)

`class Run._telemetry_get_framework(self)`


Get telemetry data for internal config structure.










## Run._make_proto_run
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L305-L326)

`class Run._make_proto_run(self, run)`


Populate protocol buffer RunData for interface/interface.










## Run.dir
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L334-L340)

`class Run.dir(self)`


str: The directory where all of the files associated with the run are
placed.











## Run.config
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L341-L347)

`class Run.config(self)`


(:obj:`Config`): A config object (similar to a nested dict) of key
value pairs associated with the hyperparameters of the run.











## Run.name
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L352-L361)

`class Run.name(self)`


str: the display name of the run. It does not need to be unique
and ideally is descriptive.










## Run.notes
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L368-L377)

`class Run.notes(self)`


str: notes associated with the run. Notes can be a multiline string
and can also use markdown and latex equations inside $$ like $\\{x}










## Run.tags
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L384-L391)

`class Run.tags(self) -> Optional[Tuple]: """Tuple[str]: tags associated with the run""" if self._tags: return self._tags run_obj = self._run_obj or self._run_obj_offline return run_obj.tags @tags.setter def tags(self, tags: Sequence): self._tags = tuple(tags) if self._backend: self._backend.interface.publish_run(self) @property def id(self)`


str: the run_id associated with the run










## Run.id
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L398-L402)

`class Run.id(self)`


str: the run_id associated with the run










## Run.sweep_id
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L403-L409)

`class Run.sweep_id(self)`


(str, optional): the sweep id associated with the run or None










## Run.path
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L410-L418)

`class Run.path(self)`


str: the path to the run [entity]/[project]/[run_id]










## Run.start_time
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L419-L426)

`class Run.start_time(self)`


int: the unix time stamp in seconds when the run started










## Run.starting_step
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L427-L434)

`class Run.starting_step(self)`


int: the first step of the run










## Run.resumed
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L435-L442)

`class Run.resumed(self)`


bool: whether or not the run was resumed










## Run.step
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L443-L451)

`class Run.step(self)`


int: step counter

Every time you call wandb.log() it will by default increment the step
counter.











## Run.mode
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L456-L460)

`class Run.mode(self)`


For compatibility with 0.9.x and earlier, deprecate eventually.










## Run.group
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L465-L478)

`class Run.group(self)`


str: name of W&B group associated with run.

Setting a group helps the W&B UI organize runs in a sensible way.

If you are doing a distributed training you should give all of the
runs in the training the same group.










## Run.project
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L484-L488)

`class Run.project(self)`


str: name of W&B project associated with run. 










## Run.get_url
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L489-L496)

`class Run.get_url(self)`

is offline







**Reutrns**

is offline


## Run.get_project_url
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L497-L504)

`class Run.get_project_url(self)`

the run or None if the run is offline







**Reutrns**

the run or None if the run is offline


## Run.get_sweep_url
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L505-L512)

`class Run.get_sweep_url(self)`

or None if there is no associated sweep or the run is offline.







**Reutrns**

or None if there is no associated sweep or the run is offline.


## Run.url
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L513-L517)

`class Run.url(self)`


str: name of W&B url associated with run.










## Run.entity
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L518-L523)

`class Run.entity(self)`


str: name of W&B entity associated with run. Entity is either
a user name or an organization name.










## Run._add_singleton
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L647-L672)

`class Run._add_singleton(self, type, key, value)`


Stores a singleton item to wandb config.

A singleton in this context is a piece of data that is continually
logged with the same value in each history step, but represented
as a single item in the config.

We do this to avoid filling up history with a lot of repeated uneccessary data

Add singleton can be called many times in one run and it will only be
updated when the value changes. The last value logged will be the one
persisted to the server










## Run.log
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L673-L807)

`class Run.log(self, data, step=None, commit=None, sync=None)`


Log a dict to the global run's history.

wandb.log can be used to log everything from scalars to histograms, media
and matplotlib plots.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|row|(dict, optional)|A dict of serializable python objects i.e str, ints, floats, Tensors, dicts, or wandb.data_types|
|commit|(boolean, optional)|Save the metrics dict to the wandb server and increment the step. If false wandb.log just updates the current metrics dict with the row argument and metrics won't be saved until wandb.log is called with commit=True.|
|step|(integer, optional)|The global step in processing. This persists any non-committed earlier steps but defaults to not committing the specified step.|
|sync|(boolean, True)|This argument is deprecated and currently doesn't change the behaviour of wandb.log|








**Example**

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

## Run.save
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L808-L893)

`class Run.save( self, glob_str: Optional[str] = None, base_path: Optional[str] = None, policy: str = "live", )`


 Ensure all files matching *glob_str* are synced to wandb with the policy specified.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|glob_str|(string)|a relative or absolute path to a unix glob or regular path. If this isn't specified the method is a noop.|
|base_path|(string)|the base path to run the glob relative to|
|policy|(string)|on of "live", "now", or "end" live: upload the file as it changes, overwriting the previous version now: upload the file once now end: only upload file when the run ends|









## Run.finish
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L903-L916)

`class Run.finish(self, exit_code=None)`


Marks a run as finished, and finishes uploading all data.  This is
used when creating multiple runs in the same process.  We automatically
call this method when your script exits.











## Run.join
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L917-L920)

`class Run.join(self, exit_code=None)`


Deprecated alias for finish() - please use finish










## Run.plot_table
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L921-L937)

`class Run.plot_table(self, vega_spec_name, data_table, fields, string_fields=None)`


Creates a custom plot on a table.

| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|vega_spec_name||the name of the spec for the plot|
|table_key||the key used to log the data table|
|data_table||a wandb.Table object containing the data to be used on the visualization|
|fields||a dict mapping from table keys to fields that the custom visualization needs|
|string_fields||a dict that provides values for any string constants the custom visualization needs|









## Run._get_sweep_url
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L973-L993)

`class Run._get_sweep_url(self)`


Generate a url for a sweep.








**Reutrns**

str - url if the run is part of a sweep
None - if the run is not part of the sweep



## Run.use_artifact
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L1553-L1606)

`class Run.use_artifact(self, artifact_or_name, type=None, aliases=None)`


 Declare an artifact as an input to a run, call `download` or `file` on \
the returned object to get the contents locally.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|artifact_or_name|(str or Artifact)|An artifact name.|
|type|(str, optional)|The type of artifact to use.|
|aliases|(list, optional)|Aliases to apply to this artifact|






**Reutrns**

A #Artifact object.



## Run.log_artifact
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L1608-L1661)

`class Run.log_artifact(self, artifact_or_path, name=None, type=None, aliases=None)`


 Declare an artifact as output of a run.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|artifact_or_path|(str or Artifact)|A path to the contents of this artifact, can be in the following forms: /local/directory /local/directory/file.txt s3://bucket/path You can also pass an Artifact object created by calling `wandb.Artifact`.|
|name|(str, optional)|An artifact name. May be prefixed with entity/project. Valid names can be in the following forms: name:version name:alias digest This will default to the basename of the path prepended with the current run id if not specified.|
|type|(str)|The type of artifact to log, examples include "dataset", "model"|
|aliases|(list, optional)|Aliases to apply to this artifact, defaults to ["latest"]|






**Reutrns**

A :obj:`Artifact` object.



## Run.alert
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L1662-L1692)

`class Run.alert(self, title, text, level=None, wait_duration=None)`


Launch an alert with the given title and text.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|title|(str)|The title of the alert, must be less than 64 characters long|
|text|(str)|The text body of the alert|
|level|(str or wandb.AlertLevel, optional)|The alert level to use, either: "INFO", "WARN", or "ERROR"|
|wait_duration|(int, float, or timedelta, optional)|The time to wait (in seconds) before sending another alert with this title|









# restore
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L1708-L1758)

`def restore( name: str, run_path: Optional[str] = None, replace: bool = False, root: Optional[str] = None, )`


 Downloads the specified file from cloud storage into the current directory
or run directory.  By default this will only download the file if it doesn't
already exist.


| **Arguments** | **Datatype** | **Description** |
|:--:|:--:|:--|
|name||the name of the file|
|run_path||optional path to a run to pull files from, i.e. username/project_name/run_id if wandb.init has not been called, this is required.|
|replace||whether to download the file even if it already exists locally|
|root||the directory to download the file to. Defaults to the current directory or the run directory if wandb.init was called.|






**Reutrns**

None if it can't find the file, otherwise a file object open for reading



# WriteSerializingFile
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/wandb_run.py#L1776-L1798)

`class WriteSerializingFile(object)`


Wrapper for a file object that serializes writes.











