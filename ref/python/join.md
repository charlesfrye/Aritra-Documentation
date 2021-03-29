# join

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/5759bab2d/wandb/sdk/wandb_run.py#L2394-L2402)




Marks a run as finished, and finishes uploading all data.

<pre><code>join(
    exit_code: int = None
) -> None</code></pre>



<!-- Placeholder for "Used in" -->

This is used when creating multiple runs in the same process.
We automatically call this method when your script exits.