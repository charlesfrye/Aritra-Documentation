description: wandb class for histograms

robots: noindex

# wandb.Histogram

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L218-L284)



wandb class for histograms

<pre>
<code>wandb.Histogram(
    sequence=None, np_histogram=None, num_bins=64
)
</code></pre>



<!-- Placeholder for "Used in" -->

This object works just like numpy's histogram function
https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html

#### Examples:

Generate histogram from a sequence
```
wandb.Histogram([1,2,3])
```

Efficiently initialize from np.histogram.
```
hist = np.histogram(data)
wandb.Histogram(np_histogram=hist)
```



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

<h3 id="from_json"><code>from_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L114-L125">View source</a>

<pre>
<code>@classmethod</code>
<code>from_json(
    json_obj, source_artifact
)
</code></pre>

Deserialize a `json_obj` into it's class representation. If additional resources were stored in the
`run_or_artifact` artifact during the `to_json` call, then those resources are expected to be in
the `source_artifact`.

<!-- Tabular view -->
 <table>
<tr><th>Args</th></tr>

</table>



<h3 id="init_from_json"><code>init_from_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L146-L168">View source</a>

<pre>
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



<h3 id="to_json"><code>to_json</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L283-L284">View source</a>

<pre>
<code>to_json(
    run=None
)
</code></pre>

Serializes the object into a JSON blob, using a run or artifact to store additional data.


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

<pre>
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

<pre>
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

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L191-L192">View source</a>

<pre>
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L194-L195">View source</a>

<pre>
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
MAX_LENGTH<a id="MAX_LENGTH"></a>
</td>
<td>
`512`
</td>
</tr><tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`None`
</td>
</tr>
</table>

