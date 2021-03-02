# finish

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/bdf4b81e3bd3af7f5cd7caf3a7d7d0244d324138/wandb/sdk/wandb_run.py#L2346-L2354)




Marks a run as finished, and finishes uploading all data.

<pre><code>finish(
    exit_code: int = None
) -> None</code></pre>



<!-- Placeholder for "Used in" -->

This is used when creating multiple runs in the same process.
We automatically call this method when your script exits.