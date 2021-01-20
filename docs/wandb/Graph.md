# wandb.Graph

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2341-L2497)



Wandb class for graphs

<pre>
<code>wandb.Graph(
    format=&#x27;keras&#x27;
)
</code></pre>



<!-- Placeholder for "Used in" -->

This class is typically used for saving and diplaying neural net models.  It
represents the graph as an array of nodes and edges.  The nodes can have
labels that can be visualized by wandb.

#### Examples:

Import a keras model:
```
>>> Graph.from_keras(keras_model)
```





<!-- Tabular view -->
 <table>
<tr><th>Attributes</th></tr>
<tr>
<td>
<code>format</code>
</td>
<td>
(string) Format to help wandb display the graph nicely.
</td>
</tr><tr>
<td>
<code>nodes</code>
</td>
<td>
([wandb.Node]) List of wandb.Nodes
</td>
</tr><tr>
<td>
<code>nodes_by_id</code>
</td>
<td>
(dict) dict of ids -> nodes
</td>
</tr><tr>
<td>
<code>edges</code>
</td>
<td>
([(wandb.Node, wandb.Node)]) List of pairs of nodes interpreted as edges
</td>
</tr><tr>
<td>
<code>loaded</code>
</td>
<td>
(boolean) Flag to tell whether the graph is completely loaded
</td>
</tr><tr>
<td>
<code>root</code>
</td>
<td>
(wandb.Node) root node of the graph
</td>
</tr>
</table>



## Methods

<h3 id="add_edge"><code>add_edge</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2423-L2427">View source</a>

<pre>
<code>add_edge(
    from_node, to_node
)
</code></pre>




<h3 id="add_node"><code>add_node</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2409-L2421">View source</a>

<pre>
<code>add_node(
    node=None, **node_kwargs
)
</code></pre>




<h3 id="from_keras"><code>from_keras</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2429-L2458">View source</a>

<pre>
<code>@classmethod</code>
<code>from_keras(
    model
)
</code></pre>




<h3 id="pprint"><code>pprint</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2403-L2407">View source</a>

<pre>
<code>pprint()
</code></pre>




<h3 id="__getitem__"><code>__getitem__</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L2400-L2401">View source</a>

<pre>
<code>__getitem__(
    nid
)
</code></pre>








<!-- Tabular view -->
 <table>
<tr><th>Class Variables</th></tr>
<tr>
<td>
artifact_type<a id="artifact_type"></a>
</td>
<td>
`None`
</td>
</tr>
</table>

