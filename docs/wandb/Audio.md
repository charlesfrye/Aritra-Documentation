description: Wandb class for audio clips.

robots: noindex

# wandb.Audio

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L753-L867)



Wandb class for audio clips.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wandb.Audio(
    data_or_path, sample_rate=None, caption=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table>
<tr><th><h2 class="add-link">Arguments</h2></th></tr>

</table>





<!-- Tabular view -->
 <table>
<tr><th><h2 class="add-link">Attributes</h2></th></tr>
<tr>
<td>
<code>artifact_source</code>
</td>
<td>
Getter which returns the object's artifact source
</td>
</tr>
</table>



## Methods

<h3 id="bind_to_run"><code>bind_to_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L334-L370">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bind_to_run(
    run, key, step, id_=None
)
</code></pre>

Bind this object to a particular Run.

Calling this function is necessary so that we have somewhere specific to
put the file associated with this object, from which other Runs can
refer to it.

<h3 id="captions"><code>captions</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L851-L857">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>captions(
    audio_list
)
</code></pre>




<h3 id="durations"><code>durations</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L843-L845">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>durations(
    audio_list
)
</code></pre>




<h3 id="file_is_set"><code>file_is_set</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L331-L332">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>file_is_set()
</code></pre>




<h3 id="from_json"><code>from_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L797-L803">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_json(
    json_obj, source_artifact
)
</code></pre>

Likely will need to override for any more complicated media objects


<h3 id="get_media_subdir"><code>get_media_subdir</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L793-L795">View source</a>

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

<!-- Tabular view -->
 <table>
<tr><th>Args</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>
<tr>
<td>
<code>wandb.Value</code>
</td>
<td>
a newly created instance of a subclass of wandb.Value
</td>
</tr>
</table>



<h3 id="is_bound"><code>is_bound</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L328-L329">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>is_bound()
</code></pre>




<h3 id="sample_rates"><code>sample_rates</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L847-L849">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>sample_rates(
    audio_list
)
</code></pre>




<h3 id="seq_to_json"><code>seq_to_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L816-L841">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>seq_to_json(
    seq, run, key, step
)
</code></pre>




<h3 id="to_json"><code>to_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L805-L814">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_json(
    run
)
</code></pre>

Serializes the object into a JSON blob, using a run or artifact to store additional data. If `run_or_artifact`
is a wandb.Run then `self.bind_to_run()` must have been previously been called.

<!-- Tabular view -->
 <table>
<tr><th>Args</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>
<tr>
<td>
<code>dict</code>
</td>
<td>
JSON representation
</td>
</tr>
</table>



<h3 id="type_mapping"><code>type_mapping</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L170-L189">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>type_mapping()
</code></pre>

Returns a map from `artifact_type` to subclass. Used to lookup correct types for deserialization.


<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>
<tr>
<td>
<code>dict</code>
</td>
<td>
dictionary of str:class
</td>
</tr>
</table>



<h3 id="with_suffix"><code>with_suffix</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L127-L144">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>with_suffix(
    name, filetype=&#x27;json&#x27;
)
</code></pre>

Helper function to return the name with suffix added if not already


<!-- Tabular view -->
 <table>
<tr><th>Args</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>
<tr>
<td>
<code>str</code>
</td>
<td>
a filename which is suffixed with it's `artifact_type` followed by the filetype
</td>
</tr>
</table>



<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L859-L864">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Likely will need to override for any more complicated media objects


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L866-L867">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.






<!-- Tabular view -->
 <table>
<tr><th><h2 class="add-link">Class Variables</h2></th></tr>
<tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`'audio-file'`
</td>
</tr>
</table>

