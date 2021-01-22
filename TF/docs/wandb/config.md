# wandb.config

<!-- Insert buttons and diff -->


[![Image](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/sdk/wandb_config.py#L24-L256)



Config object to save your run's hyperparameters.

<pre>
<code>wandb.config() -> None
</code></pre>



<!-- Placeholder for "Used in" -->

When you call <a href="../wandb/init.md"><code>wandb.init()</code></a> to start a new tracked run, a run object is saved. We recommend
saving the config object with the run at the same time, like so:
```
>>> wandb.init(config=my_config_dict)
```

You can create a file called `config-defaults.yaml`, and wandb will auto-load
your config into <a href="../wandb/config.md"><code>wandb.config</code></a>. Alternatively, you can use a YAML file with a
custom name and pass the filename:
```
>>> wandb.init(config="my_config_file.yaml")
```

See https://docs.wandb.com/library/config#file-based-configs.

#### Examples:

Basic usage
```python
wandb.config.epochs = 4
wandb.init()
for x in range(wandb.config.epochs):
    # train
```
Using wandb.init to set config
```
wandb.init(config={
    "epochs": 4,
    "batch_size": 32})
for x in range(wandb.config.epochs):
    # train
```
Nested configs
```
wandb.config['train']['epochs] = 4
wandb.init()
for x in range(wandb.config['train']['epochs']):
    # train
```
Using absl flags
```
flags.DEFINE_string(‘model’, None, ‘model to run’) # name, default, help
wandb.config.update(flags.FLAGS) # adds all absl flags to config
```
Argparse flags
```
wandb.init()
wandb.config.epochs = 4
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--batch-size', type=int, default=8, metavar='N',
                    help='input batch size for training (default: 8)')
args = parser.parse_args()
wandb.config.update(args)
```
Using TensorFlow flags (deprecated in tensorflow v2)
```
flags = tf.app.flags
flags.DEFINE_string('data_dir', '/tmp/data')
flags.DEFINE_integer('batch_size', 128, 'Batch size.')
wandb.config.update(flags.FLAGS)  # adds all of the tensorflow flags to config
```
