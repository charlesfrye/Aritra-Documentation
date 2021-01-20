description: This is a table designed to display sets of records.

robots: noindex

# wandb.Table

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L482-L750)



This is a table designed to display sets of records.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wandb.Table(
    columns=None, data=None, rows=None, dataframe=None, dtype=None, optional=True
)
</code></pre>



<!-- Placeholder for "Used in" -->


| <h2 class="add-link">Arguments</h2> | Description |
|--:|--:|
| columns ([str]): Names of the columns in the table.
Defaults to ["Input", "Output", "Expected"].
data (array): 2D Array of values that will be displayed as strings.
dataframe (pandas.DataFrame): DataFrame object used to create the table.
When set, the other arguments are ignored. |






| <h2 class="add-link">Attributes</h2> | Description |
|--:|--:|

| `artifact_source` | Getter which returns the object's artifact source |



## Methods

<h3 id="add_data"><code>add_data</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L629-L638">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_data(
    *data
)
</code></pre>

Add a row of data to the table. Argument length should match column length


<h3 id="add_row"><code>add_row</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L625-L627">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>add_row(
    *row
)
</code></pre>




<h3 id="bind_to_run"><code>bind_to_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L662-L668">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bind_to_run(
    *args, **kwargs
)
</code></pre>

Bind this object to a particular Run.

Calling this function is necessary so that we have somewhere specific to
put the file associated with this object, from which other Runs can
refer to it.

<h3 id="captions"><code>captions</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L321-L326">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>captions(
    media_items
)
</code></pre>




<h3 id="cast"><code>cast</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L588-L605">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cast(
    col_name, dtype, optional=False
)
</code></pre>




<h3 id="file_is_set"><code>file_is_set</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L331-L332">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>file_is_set()
</code></pre>




<h3 id="from_json"><code>from_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L674-L694">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_json(
    json_obj, source_artifact
)
</code></pre>

Likely will need to override for any more complicated media objects


<h3 id="get_media_subdir"><code>get_media_subdir</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L670-L672">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>get_media_subdir()
</code></pre>




<h3 id="init_from_json"><code>init_from_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L146-L168">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>init_from_json(
    json_obj, source_artifact
)
</code></pre>

Looks through all subclasses and tries to match the json obj with the class which created it. It will then
call that subclass' `from_json` method. Importantly, this function will set the return object's `source_artifact`
attribute to the passed in source artifact. This is critical for artifact bookkeeping. If you choose to create
a wandb.Value via it's `from_json` method, make sure to properly set this `artifact_source` to avoid data duplication.

| Args | Description |
|--:|--:|
| json_obj (dict): A JSON dictionary to deserialize. It must contain a `_type` key. The value of
this key is used to lookup the correct subclass to use.
source_artifact (wandb.Artifact): An artifact which will hold any additional resources which were stored
during the `to_json` function. |




| Returns | Description |
|--:|--:|

| `wandb.Value` | a newly created instance of a subclass of wandb.Value |



<h3 id="is_bound"><code>is_bound</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L328-L329">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_bound()
</code></pre>




<h3 id="to_json"><code>to_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L696-L750">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_json(
    run_or_artifact
)
</code></pre>

Serializes the object into a JSON blob, using a run or artifact to store additional data. If `run_or_artifact`
is a wandb.Run then `self.bind_to_run()` must have been previously been called.

| Args | Description |
|--:|--:|
| run_or_artifact (wandb.Run | wandb.Artifact): the Run or Artifact for which this object should be generating
JSON for - this is useful to to store additional data if needed. |




| Returns | Description |
|--:|--:|

| `dict` | JSON representation |



<h3 id="type_mapping"><code>type_mapping</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L170-L189">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>type_mapping()
</code></pre>

Returns a map from `artifact_type` to subclass. Used to lookup correct types for deserialization.


| Returns | Description |
|--:|--:|

| `dict` | dictionary of str:class |



<h3 id="with_suffix"><code>with_suffix</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L127-L144">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>with_suffix(
    name, filetype=&#x27;json&#x27;
)
</code></pre>

Helper function to return the name with suffix added if not already


| Args | Description |
|--:|--:|
| name (str): the name of the file
filetype (str, optional): the filetype to use. Defaults to "json". |




| Returns | Description |
|--:|--:|

| `str` | a filename which is suffixed with it's `artifact_type` followed by the filetype |



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L610-L623">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Likely will need to override for any more complicated media objects


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L607-L608">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.






| <h2 class="add-link">Class Variables</h2> | Description |
|--:|--:|

| MAX_ARTIFACT_ROWS | `200000` |
| MAX_ROWS | `10000` |
| artifact_type | `'table'` |

