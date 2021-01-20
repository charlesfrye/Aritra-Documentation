# wandb.save

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/sdk/wandb_run.py#L892-L981)



Ensure all files matching *glob_str* are synced to wandb with the policy specified.

<pre>
<code>wandb.save(
    glob_str: Optional[str] = None,
    base_path: Optional[str] = None,
    policy: str = &#x27;live&#x27;
) -> Union[bool, List[str]]
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

<tr>
<td>
<code>glob_str</code>
</td>
<td>
(string) a relative or absolute path to a unix glob or regular
path.  If this isn't specified the method is a noop.
</td>
</tr><tr>
<td>
<code>base_path</code>
</td>
<td>
(string) the base path to run the glob relative to
</td>
</tr><tr>
<td>
<code>policy</code>
</td>
<td>
(string) on of `live`, `now`, or `end`
- live: upload the file as it changes, overwriting the previous version
- now: upload the file once now
- end: only upload file when the run ends
</td>
</tr>
</table>

