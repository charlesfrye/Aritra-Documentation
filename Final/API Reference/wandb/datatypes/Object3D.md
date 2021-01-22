# Object3D

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/data_types.py#L877-L1040)




Wandb class for 3D point clouds.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>datatypes.Object3D(
    data_or_path, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
<table>
Arguments
<tr>
<td>
data_or_path (numpy array, string, io):
Object3D can be initialized from a file or a numpy array.

The file types supported are obj, gltf, babylon, stl.  You can pass a path to
a file or an io object and a file_type which must be one of `'obj', 'gltf', 'babylon', 'stl'`.

The shape of the numpy array must be one of either:
```
[[x y z],       ...] nx3
[x y z c],     ...] nx4 where c is a category with supported range [1, 14]
[x y z r g b], ...] nx4 where is rgb is color
```
</td>
</tr>

</table>





<!-- Tabular view -->
<table>
Class Variables

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

