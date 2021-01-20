# wandb.Table

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L482-L750)



This is a table designed to display sets of records.

<pre>
<code>wandb.Table(
    columns=None, data=None, rows=None, dataframe=None, dtype=None, optional=True
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



## Methods

<h3 id="add_data"><code>add_data</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L629-L638">View source</a>

<pre>
<code>add_data(
    *data
)
</code></pre>

Add a row of data to the table. Argument length should match column length


<h3 id="add_row"><code>add_row</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L625-L627">View source</a>

<pre>
<code>add_row(
    *row
)
</code></pre>




<h3 id="bind_to_run"><code>bind_to_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L662-L668">View source</a>

<pre>
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

<pre>
<code>@classmethod</code>
<code>captions(
    media_items
)
</code></pre>




<h3 id="cast"><code>cast</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L588-L605">View source</a>

<pre>
<code>cast(
    col_name, dtype, optional=False
)
</code></pre>




<h3 id="file_is_set"><code>file_is_set</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L331-L332">View source</a>

<pre>
<code>file_is_set()
</code></pre>




<h3 id="get_media_subdir"><code>get_media_subdir</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L670-L672">View source</a>

<pre>
<code>@classmethod</code>
<code>get_media_subdir()
</code></pre>




<h3 id="is_bound"><code>is_bound</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L328-L329">View source</a>

<pre>
<code>is_bound()
</code></pre>








<!-- Tabular view -->
 <table>
<tr><th>Class Variables</th></tr>
<tr>
<td>
MAX_ARTIFACT_ROWS<a id="MAX_ARTIFACT_ROWS"></a>
</td>
<td>
`200000`
</td>
</tr><tr>
<td>
MAX_ROWS<a id="MAX_ROWS"></a>
</td>
<td>
`10000`
</td>
</tr><tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`'table'`
</td>
</tr>
</table>

