# run

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L812-L1355)

A single run associated with an entity and project.

```text
Run(
    client, entity, project, run_id, attrs={}
)
```

| Attributes |  |
| :--- | :--- |
|  `entity` |  |
|  `id` |  |
|  `json_config` |  |
|  `lastHistoryStep` |  |
|  `name` |  |
|  `path` |  |
|  `storage_id` |  |
|  `summary` |  |
|  `url` |  |
|  `username` |  |

## Methods

### `create` <a id="create"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L894-L934)

```text
@classmethod
create(
    api, run_id=None, project=None, entity=None
)
```

Create a run for the given project

### `delete` <a id="delete"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1029-L1063)

```text
delete(
    delete_artifacts=(False)
)
```

Deletes the given run from the wandb backend.

### `file` <a id="file"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1125-L1134)

```text
file(
    name
)
```

Arguments: name \(str\): name of requested file.

| Returns |
| :--- |
|  A \`File\` matching the name argument. |

### `files` <a id="files"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1113-L1123)

```text
files(
    names=[], per_page=50
)
```

Arguments: names \(list\): names of the requested files, if empty returns all files per\_page \(int\): number of results per page

| Returns |
| :--- |
|  A \`Files\` object, which is an iterator over \`File\` obejcts. |

### `history` <a id="history"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1159-L1191)

```text
history(
    samples=500, keys=None, x_axis='_step', pandas=(True),
    stream='default'
)
```

Returns sampled history metrics for a run. This is simpler and faster if you are ok with the history records being sampled.

| Arguments |
| :--- |
|  samples \(int, optional\): The number of samples to return pandas \(bool, optional\): Return a pandas dataframe keys \(list, optional\): Only return metrics for specific keys x\_axis \(str, optional\): Use this metric as the xAxis defaults to \_step stream \(str, optional\): "default" for metrics, "system" for machine metrics |

| Returns |
| :--- |
|  If pandas=True returns a \`pandas.DataFrame\` of history metrics. If pandas=False returns a list of dicts of history metrics. |

### `load` <a id="load"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L936-L998)

```text
load(
    force=(False)
)
```

### `log_artifact` <a id="log_artifact"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1277-L1309)

```text
log_artifact(
    artifact, aliases=None
)
```

Declare an artifact as output of a run.

| Arguments |
| :--- |
|  artifact \(\`Artifact\`\): An artifact returned from \`wandb.Api\(\).artifact\(name\)\` aliases \(list, optional\): Aliases to apply to this artifact |

| Returns |
| :--- |
|  A \`Artifact\` object. |

### `logged_artifacts` <a id="logged_artifacts"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1242-L1244)

```text
logged_artifacts(
    per_page=100
)
```

### `save` <a id="save"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1065-L1066)

```text
save()
```

### `scan_history` <a id="scan_history"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1193-L1240)

```text
scan_history(
    keys=None, page_size=1000, min_step=None, max_step=None
)
```

Returns an iterable collection of all history records for a run.

#### Example:

Export all the loss values for an example run

```python
run = api.run("l2k2/examples-numpy-boston/i0wt6xua")
history = run.scan_history(keys=["Loss"])
losses = [row["Loss"] for row in history]
```

| Arguments |
| :--- |
|  keys \(\[str\], optional\): only fetch these keys, and only fetch rows that have all of keys defined. page\_size \(int, optional\): size of pages to fetch from the api |

| Returns |
| :--- |
|  An iterable collection over history records \(dict\). |

### `snake_to_camel` <a id="snake_to_camel"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L530-L532)

```text
snake_to_camel(
    string
)
```

### `update` <a id="update"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1000-L1027)

```text
update()
```

Persists changes to the run object to the wandb backend.

### `upload_file` <a id="upload_file"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1136-L1157)

```text
upload_file(
    path, root='.'
)
```

Arguments: path \(str\): name of file to upload. root \(str\): the root path to save the file relative to. i.e. If you want to have the file saved in the run as "my\_dir/file.txt" and you're currently in "my\_dir" you would set root to "../"

| Returns |
| :--- |
|  A \`File\` matching the name argument. |

### `use_artifact` <a id="use_artifact"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1250-L1275)

```text
use_artifact(
    artifact
)
```

Declare an artifact as an input to a run.

| Arguments |
| :--- |
|  artifact \(\`Artifact\`\): An artifact returned from \`wandb.Api\(\).artifact\(name\)\` |

| Returns |
| :--- |
|  A \`Artifact\` object. |

### `used_artifacts` <a id="used_artifacts"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/apis/public.py#L1246-L1248)

```text
used_artifacts(
    per_page=100
)
```

