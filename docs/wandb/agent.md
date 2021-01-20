description: Generic agent entrypoint, used for CLI or jupyter.

robots: noindex

# wandb.agent

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/wandb_agent.py#L525-L568)



Generic agent entrypoint, used for CLI or jupyter.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>wandb.agent(
    sweep_id, function=None, entity=None, project=None, count=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Will run a function or program with configuration parameters specified
    by server.

<!-- Tabular view -->
 <table>
<tr><th>Arguments</th></tr>

</table>



#### Examples:

Run a sample sweep over a function:
def train():
    with wandb.init() as run:
        print("config:", dict(run.config))
        for epoch in range(35):
            print("running", epoch)
            wandb.log({"metric": run.config.param1, "epoch": epoch})
            time.sleep(1)

wandb.agent(sweep_id, function=train)
