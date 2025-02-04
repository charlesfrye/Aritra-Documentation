# Run

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L169-L2269)




The run object corresponds to a single execution of your script,

<pre><code>Run(
    settings: Settings,
    config: Optional[Dict[str, Any]] = None,
    sweep_config: Optional[Dict[str, Any]] = None
) -> None</code></pre>



<!-- Placeholder for "Used in" -->
typically this is an ML experiment. Create a run with `wandb.init()`.

In distributed training, use `wandb.init()` to create a run for each process,
and set the group argument to organize runs into a larger experiment.

Currently there is a parallel Run object in the wandb.Api. Eventually these
two objects will be merged.



<!-- Tabular view -->
<table>
<tr><th>Attributes</th></tr>

<tr>
<td>
<code>history</code>
</td>
<td>
(History) Time series values, created with `wandb.log()`.
History can contain scalar values, rich media, or even custom plots
across multiple steps.
</td>
</tr><tr>
<td>
<code>summary</code>
</td>
<td>
(Summary) Single values set for each `wandb.log()` key. By
default, summary is set to the last value logged. You can manually
set summary to the best value, like max accuracy, instead of the
final value.
</td>
</tr><tr>
<td>
<code>config</code>
</td>
<td>
Returns:
(Config): A config object (similar to a nested dict) of key
value pairs associated with the hyperparameters of the run.
</td>
</tr><tr>
<td>
<code>config_static</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>dir</code>
</td>
<td>
Returns:
(str): The directory where all of the files associated with the run are
placed.
</td>
</tr><tr>
<td>
<code>disabled</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>entity</code>
</td>
<td>
Returns:
(str): name of W&B entity associated with run. Entity is either
a user name or an organization name.
</td>
</tr><tr>
<td>
<code>group</code>
</td>
<td>
Setting a group helps the W&B UI organize runs in a sensible way.

If you are doing a distributed training you should give all of the
runs in the training the same group.
If you are doing crossvalidation you should give all the crossvalidation
folds the same group.
</td>
</tr><tr>
<td>
<code>id</code>
</td>
<td>
id property.
</td>
</tr><tr>
<td>
<code>job_type</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>mode</code>
</td>
<td>
For compatibility with `0.9.x` and earlier, deprecate eventually.
</td>
</tr><tr>
<td>
<code>name</code>
</td>
<td>
Returns:
(str): the display name of the run. It does not need to be unique
and ideally is descriptive.
</td>
</tr><tr>
<td>
<code>notes</code>
</td>
<td>
Returns:
(str): notes associated with the run. Notes can be a multiline string
and can also use markdown and latex equations inside $$ like $\\{x}
</td>
</tr><tr>
<td>
<code>offline</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>path</code>
</td>
<td>
Returns:
(str): the path to the run `[entity]/[project]/[run_id]`
</td>
</tr><tr>
<td>
<code>project</code>
</td>
<td>
Returns:
(str): name of W&B project associated with run.
</td>
</tr><tr>
<td>
<code>resumed</code>
</td>
<td>
Returns:
(bool): whether or not the run was resumed
</td>
</tr><tr>
<td>
<code>start_time</code>
</td>
<td>
Returns:
(int): the unix time stamp in seconds when the run started
</td>
</tr><tr>
<td>
<code>starting_step</code>
</td>
<td>
Returns:
(int): the first step of the run
</td>
</tr><tr>
<td>
<code>step</code>
</td>
<td>
Every time you call wandb.log() it will by default increment the step
counter.
</td>
</tr><tr>
<td>
<code>sweep_id</code>
</td>
<td>
Returns:
(str, optional): the sweep id associated with the run or None
</td>
</tr><tr>
<td>
<code>tags</code>
</td>
<td>
Returns:
(Tuple[str]): tags associated with the run
</td>
</tr><tr>
<td>
<code>url</code>
</td>
<td>
Returns:
(str): name of W&B url associated with run.
</td>
</tr>
</table>



## Methods

<h3 id="alert"><code>alert</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L2220-L2256">View source</a>

<pre><code>alert(
    title: str,
    text: str,
    level: Union[str, None] = None,
    wait_duration: Union[int, float, timedelta, None] = None
) -> None</code></pre>

Launch an alert with the given title and text.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>title</code>
</td>
<td>
(str) The title of the alert, must be less than 64 characters long.
</td>
</tr><tr>
<td>
<code>text</code>
</td>
<td>
(str) The text body of the alert.
</td>
</tr><tr>
<td>
<code>level</code>
</td>
<td>
(str or wandb.AlertLevel, optional) The alert level to use, either: `INFO`, `WARN`, or `ERROR`.
</td>
</tr><tr>
<td>
<code>wait_duration</code>
</td>
<td>
(int, float, or timedelta, optional) The time to wait (in seconds) before sending another
alert with this title.
</td>
</tr>
</table>



<h3 id="finish"><code>finish</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1127-L1142">View source</a>

<pre><code>finish(
    exit_code: int = None
) -> None</code></pre>

Marks a run as finished, and finishes uploading all data.  This is
used when creating multiple runs in the same process.  We automatically
call this method when your script exits.

<h3 id="finish_artifact"><code>finish_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L2069-L2118">View source</a>

<pre><code>finish_artifact(
    artifact_or_path: Union[<a href="../library/Artifact.md"><code>library.Artifact</code></a>, str],
    name: Optional[str] = None,
    type: Optional[str] = None,
    aliases: Optional[List[str]] = None,
    distributed_id: Optional[str] = None
) -> <a href="../library/Artifact.md"><code>library.Artifact</code></a></code></pre>

Finish a non-finalized artifact as output of a run. Subsequent "upserts" with
the same distributed ID will result in a new version

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
artifact_or_path (str or Artifact): A path to the contents of this artifact,
can be in the following forms:
- `/local/directory`
- `/local/directory/file.txt`
- `s3://bucket/path`
You can also pass an Artifact object created by calling
`wandb.Artifact`.
name (str, optional): An artifact name. May be prefixed with entity/project.
Valid names can be in the following forms:
- name:version
- name:alias
- digest
This will default to the basename of the path prepended with the current
run id  if not specified.
type (str): The type of artifact to log, examples include `dataset`, `model`
aliases (list, optional): Aliases to apply to this artifact,
defaults to `["latest"]`
distributed_id (string, optional): Unique string that all distributed jobs share. If None,
defaults to the run's group name.
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An `Artifact` object.
</td>
</tr>

</table>



<h3 id="get_project_url"><code>get_project_url</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L678-L687">View source</a>

<pre><code>get_project_url() -> Optional[str]</code></pre>

Returns:
    (str, optional): url for the W&B project associated with
        the run or None if the run is offline

<h3 id="get_sweep_url"><code>get_sweep_url</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L689-L698">View source</a>

<pre><code>get_sweep_url() -> Optional[str]</code></pre>

Returns:
    (str, optional): url for the sweep associated with the run
        or None if there is no associated sweep or the run is offline.

<h3 id="get_url"><code>get_url</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L667-L676">View source</a>

<pre><code>get_url() -> Optional[str]</code></pre>

Returns:
    (str, optional): url for the W&B run or None if the run
        is offline

<h3 id="join"><code>join</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1144-L1146">View source</a>

<pre><code>join(
    exit_code: int = None
) -> None</code></pre>

Deprecated alias for `finish()` - please use finish


<h3 id="log"><code>log</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L877-L1025">View source</a>

<pre><code>log(
    data: Dict[str, Any],
    step: int = None,
    commit: bool = None,
    sync: bool = None
) -> None</code></pre>

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

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
row (dict, optional): A dict of serializable python objects i.e `str`,
`ints`, `floats`, `Tensors`, `dicts`, or `wandb.data_types`.
commit (boolean, optional): Save the metrics dict to the wandb server
and increment the step.  If false `wandb.log` just updates the current
metrics dict with the row argument and metrics won't be saved until
`wandb.log` is called with `commit=True`.
step (integer, optional): The global step in processing. This persists
any non-committed earlier steps but defaults to not committing the
specified step.
sync (boolean, True): This argument is deprecated and currently doesn't
change the behaviour of `wandb.log`.
</td>
</tr>

</table>



#### Examples:

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



<!-- Tabular view -->
<table>
<tr><th>Raises</th></tr>
<tr>
<td>
wandb.Error - if called before `wandb.init`
ValueError - if invalid data is passed
</td>
</tr>

</table>



<h3 id="log_artifact"><code>log_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1985-L2016">View source</a>

<pre><code>log_artifact(
    artifact_or_path: Union[<a href="../library/Artifact.md"><code>library.Artifact</code></a>, str],
    name: Optional[str] = None,
    type: Optional[str] = None,
    aliases: Optional[List[str]] = None
) -> <a href="../library/Artifact.md"><code>library.Artifact</code></a></code></pre>

Declare an artifact as output of a run.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
artifact_or_path (str or Artifact): A path to the contents of this artifact,
can be in the following forms:
- `/local/directory`
- `/local/directory/file.txt`
- `s3://bucket/path`
You can also pass an Artifact object created by calling
`wandb.Artifact`.
name (str, optional): An artifact name. May be prefixed with entity/project.
Valid names can be in the following forms:
- name:version
- name:alias
- digest
This will default to the basename of the path prepended with the current
run id  if not specified.
type (str): The type of artifact to log, examples include `dataset`, `model`
aliases (list, optional): Aliases to apply to this artifact,
defaults to `["latest"]`
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An `Artifact` object.
</td>
</tr>

</table>



<h3 id="log_code"><code>log_code</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L608-L665">View source</a>

<pre><code>log_code(
    root: str = &#x27;.&#x27;,
    name: str = None,
    include_fn: Callable[[str], bool] = (lambda path: path.endswith(&#x27;.py&#x27;)),
    exclude_fn: Callable[[str], bool] = (lambda path: os.sep + &#x27;wandb&#x27; + os.sep in path)
) -> Optional[<a href="../library/Artifact.md"><code>library.Artifact</code></a>]</code></pre>

log_code() saves the current state of your code to a W&B artifact.  By
default it walks the current directory and logs all files that end with ".py".

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
root (str, optional): The relative (to os.getcwd()) or absolute path to
recursively find code from.
name (str, optional): The name of our code artifact.  By default we'll name
the artifact "source-$RUN_ID".  There may be scenarios where you want
many runs to share the same artifact.  Specifying name allows you to achieve that.
include_fn (callable, optional): A callable that accepts a file path and
returns True when it should be included and False otherwise.  This
defaults to: `lambda path: path.endswith(".py")`
exclude_fn (callable, optional): A callable that accepts a file path and
returns True when it should be excluded and False otherwise.  This
defaults to: `lambda path: False`
</td>
</tr>

</table>



#### Examples:

Basic usage
```
run.log_code()
```

Advanced usage
```
run.log_code("../", include_fn=lambda path: path.endswith(".py") or path.endswith(".ipynb"))
```



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An `Artifact` object if code was logged
</td>
</tr>

</table>



<h3 id="plot_table"><code>plot_table</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1149-L1164">View source</a>

<pre><code>plot_table(
    vega_spec_name, data_table, fields, string_fields=None
)</code></pre>

Creates a custom plot on a table.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>vega_spec_name</code>
</td>
<td>
the name of the spec for the plot
</td>
</tr><tr>
<td>
<code>table_key</code>
</td>
<td>
the key used to log the data table
</td>
</tr><tr>
<td>
<code>data_table</code>
</td>
<td>
a wandb.Table object containing the data to
be used on the visualization
</td>
</tr><tr>
<td>
<code>fields</code>
</td>
<td>
a dict mapping from table keys to fields that the custom
visualization needs
</td>
</tr><tr>
<td>
<code>string_fields</code>
</td>
<td>
a dict that provides values for any string constants
the custom visualization needs
</td>
</tr>
</table>



<h3 id="project_name"><code>project_name</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L562-L564">View source</a>

<pre><code>project_name() -> str</code></pre>




<h3 id="restore"><code>restore</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1118-L1125">View source</a>

<pre><code>restore(
    name: str,
    run_path: Optional[str] = None,
    replace: bool = (False),
    root: Optional[str] = None
) -> Union[None, TextIO]</code></pre>

Downloads the specified file from cloud storage into the current directory
or run directory.  By default this will only download the file if it doesn't
already exist.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>name</code>
</td>
<td>
the name of the file
</td>
</tr><tr>
<td>
<code>run_path</code>
</td>
<td>
optional path to a run to pull files from, i.e. `username/project_name/run_id`
if wandb.init has not been called, this is required.
</td>
</tr><tr>
<td>
<code>replace</code>
</td>
<td>
whether to download the file even if it already exists locally
</td>
</tr><tr>
<td>
<code>root</code>
</td>
<td>
the directory to download the file to.  Defaults to the current
directory or the run directory if wandb.init was called.
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
None if it can't find the file, otherwise a file object open for reading
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Raises</th></tr>

<tr>
<td>
<code>wandb.CommError</code>
</td>
<td>
if we can't connect to the wandb backend
</td>
</tr><tr>
<td>
<code>ValueError</code>
</td>
<td>
if the file is not found or can't find run_path
</td>
</tr>
</table>



<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1027-L1116">View source</a>

<pre><code>save(
    glob_str: Optional[str] = None,
    base_path: Optional[str] = None,
    policy: str = &#x27;live&#x27;
) -> Union[bool, List[str]]</code></pre>

Ensure all files matching *glob_str* are synced to wandb with the policy specified.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
glob_str (string): a relative or absolute path to a unix glob or regular
path.  If this isn't specified the method is a noop.
base_path (string): the base path to run the glob relative to
policy (string): on of `live`, `now`, or `end`
- live: upload the file as it changes, overwriting the previous version
- now: upload the file once now
- end: only upload file when the run ends
</td>
</tr>

</table>



<h3 id="upsert_artifact"><code>upsert_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L2018-L2067">View source</a>

<pre><code>upsert_artifact(
    artifact_or_path: Union[<a href="../library/Artifact.md"><code>library.Artifact</code></a>, str],
    name: Optional[str] = None,
    type: Optional[str] = None,
    aliases: Optional[List[str]] = None,
    distributed_id: Optional[str] = None
) -> <a href="../library/Artifact.md"><code>library.Artifact</code></a></code></pre>

Declare (or append tp) a non-finalized artifact as output of a run. Note that you must call
run.finish_artifact() to finalize the artifact. This is useful when distributed jobs
need to all contribute to the same artifact.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
artifact_or_path (str or Artifact): A path to the contents of this artifact,
can be in the following forms:
- `/local/directory`
- `/local/directory/file.txt`
- `s3://bucket/path`
You can also pass an Artifact object created by calling
`wandb.Artifact`.
name (str, optional): An artifact name. May be prefixed with entity/project.
Valid names can be in the following forms:
- name:version
- name:alias
- digest
This will default to the basename of the path prepended with the current
run id  if not specified.
type (str): The type of artifact to log, examples include `dataset`, `model`
aliases (list, optional): Aliases to apply to this artifact,
defaults to `["latest"]`
distributed_id (string, optional): Unique string that all distributed jobs share. If None,
defaults to the run's group name.
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An `Artifact` object.
</td>
</tr>

</table>



<h3 id="use_artifact"><code>use_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1933-L1983">View source</a>

<pre><code>use_artifact(
    artifact_or_name, type=None, aliases=None
)</code></pre>

Declare an artifact as an input to a run, call `download` or `file` on
the returned object to get the contents locally.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>
<tr>
<td>
artifact_or_name (str or Artifact): An artifact name.
May be prefixed with entity/project. Valid names
can be in the following forms:
- name:version
- name:alias
- digest
You can also pass an Artifact object created by calling `wandb.Artifact`
type (str, optional): The type of artifact to use.
aliases (list, optional): Aliases to apply to this artifact
</td>
</tr>

</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An `Artifact` object.
</td>
</tr>

</table>



<h3 id="watch"><code>watch</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L1929-L1930">View source</a>

<pre><code>watch(
    models, criterion=None, log=&#x27;gradients&#x27;, log_freq=100, idx=None
) -> None</code></pre>






