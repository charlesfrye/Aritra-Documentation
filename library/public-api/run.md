# Run

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L812-L1355)




A single run associated with an entity and project.

<pre><code>Run(
    client, entity, project, run_id, attrs={}
)</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
<table>
<tr><th>Attributes</th></tr>

<tr>
<td>
<code>tags</code>
</td>
<td>
([str]) a list of tags associated with the run
</td>
</tr><tr>
<td>
<code>url</code>
</td>
<td>
(str) the url of this run
</td>
</tr><tr>
<td>
<code>id</code>
</td>
<td>
(str) unique identifier for the run (defaults to eight characters)
</td>
</tr><tr>
<td>
<code>name</code>
</td>
<td>
(str) the name of the run
</td>
</tr><tr>
<td>
<code>state</code>
</td>
<td>
(str) one of: running, finished, crashed, aborted
</td>
</tr><tr>
<td>
<code>config</code>
</td>
<td>
(dict) a dict of hyperparameters associated with the run
</td>
</tr><tr>
<td>
<code>created_at</code>
</td>
<td>
(str) ISO timestamp when the run was started
</td>
</tr><tr>
<td>
<code>system_metrics</code>
</td>
<td>
(dict) the latest system metrics recorded for the run
</td>
</tr><tr>
<td>
<code>summary</code>
</td>
<td>
(dict) A mutable dict-like property that holds the current summary.
Calling update will persist any changes.
</td>
</tr><tr>
<td>
<code>project</code>
</td>
<td>
(str) the project associated with the run
</td>
</tr><tr>
<td>
<code>entity</code>
</td>
<td>
(str) the name of the entity associated with the run
</td>
</tr><tr>
<td>
<code>user</code>
</td>
<td>
(str) the name of the user who created the run
</td>
</tr><tr>
<td>
<code>path</code>
</td>
<td>
(str) Unique identifier [entity]/[project]/[run_id]
</td>
</tr><tr>
<td>
<code>notes</code>
</td>
<td>
(str) Notes about the run
</td>
</tr><tr>
<td>
<code>read_only</code>
</td>
<td>
(boolean) Whether the run is editable
</td>
</tr><tr>
<td>
<code>history_keys</code>
</td>
<td>
(str) Keys of the history metrics that have been logged
with `wandb.log({key: value})`
</td>
</tr><tr>
<td>
<code>json_config</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>lastHistoryStep</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>storage_id</code>
</td>
<td>

</td>
</tr><tr>
<td>
<code>username</code>
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="create"><code>create</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L894-L934">View source</a>

<pre><code>@classmethod</code>
<code>create(
    api, run_id=None, project=None, entity=None
)</code></pre>

Create a run for the given project


<h3 id="delete"><code>delete</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1029-L1063">View source</a>

<pre><code>delete(
    delete_artifacts=(False)
)</code></pre>

Deletes the given run from the wandb backend.


<h3 id="file"><code>file</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1125-L1134">View source</a>

<pre><code>file(
    name
)</code></pre>

Arguments:
    name: (str) name of requested file.

<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `File` matching the name argument.
</td>
</tr>

</table>



<h3 id="files"><code>files</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1113-L1123">View source</a>

<pre><code>files(
    names=[], per_page=50
)</code></pre>

Arguments:
    names: (list) names of the requested files, if empty returns all files
    per_page: (int) number of results per page

<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `Files` object, which is an iterator over `File` obejcts.
</td>
</tr>

</table>



<h3 id="history"><code>history</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1159-L1191">View source</a>

<pre><code>history(
    samples=500, keys=None, x_axis=&#x27;_step&#x27;, pandas=(True),
    stream=&#x27;default&#x27;
)</code></pre>

Returns sampled history metrics for a run.  This is simpler and faster if you are ok with
the history records being sampled.

<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>samples</code>
</td>
<td>
(int, optional) The number of samples to return
</td>
</tr><tr>
<td>
<code>pandas</code>
</td>
<td>
(bool, optional) Return a pandas dataframe
</td>
</tr><tr>
<td>
<code>keys</code>
</td>
<td>
(list, optional) Only return metrics for specific keys
</td>
</tr><tr>
<td>
<code>x_axis</code>
</td>
<td>
(str, optional) Use this metric as the xAxis defaults to _step
</td>
</tr><tr>
<td>
<code>stream</code>
</td>
<td>
(str, optional) "default" for metrics, "system" for machine metrics
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
If pandas=True returns a `pandas.DataFrame` of history metrics.
If pandas=False returns a list of dicts of history metrics.
</td>
</tr>

</table>



<h3 id="load"><code>load</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L936-L998">View source</a>

<pre><code>load(
    force=(False)
)</code></pre>




<h3 id="log_artifact"><code>log_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1277-L1309">View source</a>

<pre><code>log_artifact(
    artifact, aliases=None
)</code></pre>

Declare an artifact as output of a run.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>artifact</code>
</td>
<td>
(`Artifact`) An artifact returned from
`wandb.Api().artifact(name)`
</td>
</tr><tr>
<td>
<code>aliases</code>
</td>
<td>
(list, optional) Aliases to apply to this artifact
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `Artifact` object.
</td>
</tr>

</table>



<h3 id="logged_artifacts"><code>logged_artifacts</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1242-L1244">View source</a>

<pre><code>logged_artifacts(
    per_page=100
)</code></pre>




<h3 id="save"><code>save</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1065-L1066">View source</a>

<pre><code>save()</code></pre>




<h3 id="scan_history"><code>scan_history</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1193-L1240">View source</a>

<pre><code>scan_history(
    keys=None, page_size=1000, min_step=None, max_step=None
)</code></pre>

Returns an iterable collection of all history records for a run.


#### Example:

Export all the loss values for an example run

```python
run = api.run("l2k2/examples-numpy-boston/i0wt6xua")
history = run.scan_history(keys=["Loss"])
losses = [row["Loss"] for row in history]
```




<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>keys</code>
</td>
<td>
([str], optional) only fetch these keys, and only fetch rows that have all of keys defined.
</td>
</tr><tr>
<td>
<code>page_size</code>
</td>
<td>
(int, optional) size of pages to fetch from the api
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
An iterable collection over history records (dict).
</td>
</tr>

</table>



<h3 id="snake_to_camel"><code>snake_to_camel</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L530-L532">View source</a>

<pre><code>snake_to_camel(
    string
)</code></pre>




<h3 id="update"><code>update</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1000-L1027">View source</a>

<pre><code>update()</code></pre>

Persists changes to the run object to the wandb backend.


<h3 id="upload_file"><code>upload_file</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1136-L1157">View source</a>

<pre><code>upload_file(
    path, root=&#x27;.&#x27;
)</code></pre>

Arguments:
    path: (str) name of file to upload.
    root: (str) the root path to save the file relative to.  i.e.
        If you want to have the file saved in the run as "my_dir/file.txt"
        and you're currently in "my_dir" you would set root to "../"

<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `File` matching the name argument.
</td>
</tr>

</table>



<h3 id="use_artifact"><code>use_artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1250-L1275">View source</a>

<pre><code>use_artifact(
    artifact
)</code></pre>

Declare an artifact as an input to a run.


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>artifact</code>
</td>
<td>
(`Artifact`) An artifact returned from
`wandb.Api().artifact(name)`
</td>
</tr>
</table>



<!-- Tabular view -->
<table>
<tr><th>Returns</th></tr>
<tr>
<td>
A `Artifact` object.
</td>
</tr>

</table>



<h3 id="used_artifacts"><code>used_artifacts</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L1246-L1248">View source</a>

<pre><code>used_artifacts(
    per_page=100
)</code></pre>






