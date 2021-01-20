# wandb.Object3D

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L877-L1040)



Wandb class for 3D point clouds.

<pre>
<code>wandb.Object3D(
    data_or_path, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



## Methods

<h3 id="bind_to_run"><code>bind_to_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L334-L370">View source</a>

<pre>
<code>bind_to_run(
    run, key, step, id_=None
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




<h3 id="file_is_set"><code>file_is_set</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L331-L332">View source</a>

<pre>
<code>file_is_set()
</code></pre>




<h3 id="get_media_subdir"><code>get_media_subdir</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1000-L1002">View source</a>

<pre>
<code>@classmethod</code>
<code>get_media_subdir()
</code></pre>




<h3 id="is_bound"><code>is_bound</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L328-L329">View source</a>

<pre>
<code>is_bound()
</code></pre>




<h3 id="seq_to_json"><code>seq_to_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1018-L1040">View source</a>

<pre>
<code>@classmethod</code>
<code>seq_to_json(
    three_d_list, run, key, step
)
</code></pre>








<!-- Tabular view -->
 <table>
<tr><th>Class Variables</th></tr>
<tr>
<td>
SUPPORTED_TYPES<a id="SUPPORTED_TYPES"></a>
</td>
<td>

</td>
</tr><tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`'object3D-file'`
</td>
</tr>
</table>

