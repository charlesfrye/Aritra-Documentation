# finish

<!-- Insert buttons and diff -->


[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/wandb_run.py#L2362-L2370)




Marks a run as finished, and finishes uploading all data.

<pre><code>finish(
    exit_code: int = None
) -> None</code></pre>



<!-- Placeholder for "Used in" -->

This is used when creating multiple runs in the same process.
We automatically call this method when your script exits.