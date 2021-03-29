# Table

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L125-L603)




This is a table designed to display sets of records.

<pre><code>Table(
    columns=None, data=None, rows=None, dataframe=None, dtype=None, optional=(True),
    allow_mixed_types=(False)
)</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>columns</code>
</td>
<td>
([str]) Names of the columns in the table.
Defaults to ["Input", "Output", "Expected"].
</td>
</tr><tr>
<td>
<code>data</code>
</td>
<td>
(array) 2D Array of values that will be displayed as strings.
</td>
</tr><tr>
<td>
<code>dataframe</code>
</td>
<td>
(pandas.DataFrame) DataFrame object used to create the table.
When set, the other arguments are ignored.
optional (Union[bool,List[bool]]): If None values are allowed. Singular bool
applies to all columns. A list of bool values applies to each respective column.
Default to True.
allow_mixed_types (bool): Determines if columns are allowed to have mixed types (disables type validation). Defaults to False
</td>
</tr>
</table>



## Methods

<h3 id="add_data"><code>add_data</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L339-L366">View source</a>

<pre><code>add_data(
    *data
)</code></pre>

Add a row of data to the table. Argument length should match column length


<h3 id="add_row"><code>add_row</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L335-L337">View source</a>

<pre><code>add_row(
    *row
)</code></pre>




<h3 id="cast"><code>cast</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L240-L293">View source</a>

<pre><code>cast(
    col_name, dtype, optional=(False)
)</code></pre>

Casts a column to a specific type


<!-- Tabular view -->
<table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>col_name</code>
</td>
<td>
(str) - name of the column to cast
</td>
</tr><tr>
<td>
<code>dtype</code>
</td>
<td>
(class, wandb.wandb_sdk.interface._dtypes.Type, any) - the target dtype. Can be one of
normal python class, internal WB type, or an example object (eg. an instance of wandb.Image or wandb.Classes)
</td>
</tr><tr>
<td>
<code>optional</code>
</td>
<td>
(bool) - if the column should allow Nones
</td>
</tr>
</table>



<h3 id="iterrows"><code>iterrows</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L484-L497">View source</a>

<pre><code>iterrows()</code></pre>

Iterate over rows as (ndx, row)
Yields
------
index : int
    The index of the row. Using this value in other WandB tables
    will automatically build a relationship between the tables
row : List[any]
    The data of the row

<h3 id="set_fk"><code>set_fk</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L504-L508">View source</a>

<pre><code>set_fk(
    col_name, table, table_col
)</code></pre>




<h3 id="set_pk"><code>set_pk</code></h3>

<a target="_blank" href="https://www.github.com/wandb/client/tree/5759bab2d/wandb/data_types.py#L499-L502">View source</a>

<pre><code>set_pk(
    col_name
)</code></pre>








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

