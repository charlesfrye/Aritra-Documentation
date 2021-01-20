description: Used for querying the wandb server.

robots: noindex

# wandb.Api

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L181-L515)



Used for querying the wandb server.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wandb.Api(
    overrides={}
)
</code></pre>



<!-- Placeholder for "Used in" -->


#### Examples:

Most common way to initialize
```
    wandb.Api()
```



<!-- Tabular view -->
 <table>
<tr><th><h2 class="add-link">Arguments</h2></th></tr>

</table>





<!-- Tabular view -->
 <table>
<tr><th><h2 class="add-link">Attributes</h2></th></tr>
<tr>
<td style="text-align:left;">
`api_key`
</td>
<td style="text-align:left;">

</td>
</tr><tr>
<td style="text-align:left;">
`client`
</td>
<td style="text-align:left;">

</td>
</tr><tr>
<td style="text-align:left;">
`default_entity`
</td>
<td style="text-align:left;">

</td>
</tr><tr>
<td style="text-align:left;">
`user_agent`
</td>
<td style="text-align:left;">

</td>
</tr>
</table>



## Methods

<h3 id="artifact"><code>artifact</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L495-L515">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>artifact(
    name, type=None
)
</code></pre>

Returns a single artifact by parsing path in the form entity/project/run_id.


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>

</table>



<h3 id="artifact_type"><code>artifact_type</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L484-L487">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>artifact_type(
    type_name, project=None
)
</code></pre>




<h3 id="artifact_types"><code>artifact_types</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L479-L482">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>artifact_types(
    project=None
)
</code></pre>




<h3 id="artifact_versions"><code>artifact_versions</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L489-L493">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>artifact_versions(
    type_name, name, per_page=50
)
</code></pre>




<h3 id="create_run"><code>create_run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L245-L248">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>create_run(
    **kwargs
)
</code></pre>




<h3 id="flush"><code>flush</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L276-L281">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>flush()
</code></pre>

The api object keeps a local cache of runs, so if the state of the run may
    change while executing your script you must clear the local cache with `api.flush()`
    to get the latest values associated with the run.

<h3 id="projects"><code>projects</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L338-L358">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>projects(
    entity=None, per_page=200
)
</code></pre>

Get projects for a given entity.


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>

</table>



<h3 id="reports"><code>reports</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L360-L391">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>reports(
    path=&#x27;&#x27;, name=None, per_page=50
)
</code></pre>

Get reports for a given project path.

WARNING: This api is in beta and will likely change in a future release

<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>

</table>



<h3 id="run"><code>run</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L444-L459">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>run(
    path=&#x27;&#x27;
)
</code></pre>

Returns a single run by parsing path in the form entity/project/run_id.


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>

</table>



<h3 id="runs"><code>runs</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L393-L442">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>runs(
    path=&#x27;&#x27;, filters={}, order=&#x27;-created_at&#x27;, per_page=50
)
</code></pre>

Return a set of runs from a project that match the filters provided.
You can filter by `config.*`, `summary.*`, `state`, `entity`, `createdAt`, etc.

#### Examples:

Find runs in my_project config.experiment_name has been set to "foo"
```
api.runs(path="my_entity/my_project", {"config.experiment_name": "foo"})
```

Find runs in my_project config.experiment_name has been set to "foo" or "bar"
```
api.runs(path="my_entity/my_project",
    {"$or": [{"config.experiment_name": "foo"}, {"config.experiment_name": "bar"}]})
```

Find runs in my_project sorted by ascending loss
```
api.runs(path="my_entity/my_project", {"order": "+summary_metrics.loss"})
```




<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>

</table>



<h3 id="sweep"><code>sweep</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L461-L477">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>sweep(
    path=&#x27;&#x27;
)
</code></pre>

Returns a sweep by parsing path in the form entity/project/sweep_id.


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



<!-- Tabular view -->
 <table>
<tr><th>Returns</th></tr>

</table>







<!-- Tabular view -->
 <table>
<tr><th><h2 class="add-link">Class Variables</h2></th></tr>
<tr>
<td style="text-align:left;">
VIEWER_QUERY<a id="VIEWER_QUERY"></a>
</td>
<td style="text-align:left;">

</td>
</tr>
</table>

