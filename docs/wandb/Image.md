# wandb.Image

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1526-L1941)



Wandb class for images.

<pre>
<code>wandb.Image(
    data_or_path, mode=None, caption=None, grouping=None, classes=None, boxes=None,
    masks=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



## Methods

<h3 id="all_boxes"><code>all_boxes</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1906-L1921">View source</a>

<pre>
<code>@classmethod</code>
<code>all_boxes(
    images, run, run_key, step
)
</code></pre>




<h3 id="all_captions"><code>all_captions</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1923-L1928">View source</a>

<pre>
<code>@classmethod</code>
<code>all_captions(
    images
)
</code></pre>




<h3 id="all_masks"><code>all_masks</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1889-L1904">View source</a>

<pre>
<code>@classmethod</code>
<code>all_masks(
    images, run, run_key, step
)
</code></pre>




<h3 id="bind_to_run"><code>bind_to_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1720-L1731">View source</a>

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




<h3 id="file_is_set"><code>file_is_set</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L331-L332">View source</a>

<pre>
<code>file_is_set()
</code></pre>




<h3 id="get_media_subdir"><code>get_media_subdir</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1716-L1718">View source</a>

<pre>
<code>@classmethod</code>
<code>get_media_subdir()
</code></pre>




<h3 id="guess_mode"><code>guess_mode</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1791-L1805">View source</a>

<pre>
<code>guess_mode(
    data
)
</code></pre>

Guess what type of image the np.array is representing


<h3 id="is_bound"><code>is_bound</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L328-L329">View source</a>

<pre>
<code>is_bound()
</code></pre>




<h3 id="seq_to_json"><code>seq_to_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1831-L1887">View source</a>

<pre>
<code>@classmethod</code>
<code>seq_to_json(
    images, run, key, step
)
</code></pre>

Combines a list of images into a meta dictionary object describing the child images.


<h3 id="to_uint8"><code>to_uint8</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L1807-L1829">View source</a>

<pre>
<code>@classmethod</code>
<code>to_uint8(
    data
)
</code></pre>

Converts floating point image on the range [0,1] and integer images
on the range [0,255] to uint8, clipping if necessary.





<!-- Tabular view -->
 <table>
<tr><th>Class Variables</th></tr>
<tr>
<td>
MAX_DIMENSION<a id="MAX_DIMENSION"></a>
</td>
<td>
`65500`
</td>
</tr><tr>
<td>
MAX_ITEMS<a id="MAX_ITEMS"></a>
</td>
<td>
`108`
</td>
</tr><tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`'image-file'`
</td>
</tr>
</table>

