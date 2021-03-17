# audio

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/data_types.py#L490-L628)

Wandb class for audio clips.

```text
Audio(
    data_or_path, sample_rate=None, caption=None
)
```

| Arguments |  |
| :--- | :--- |
|  `data_or_path` |  \(string or numpy array\) A path to an audio file or a numpy array of audio data. |
|  `sample_rate` |  \(int\) Sample rate, required when passing in raw numpy array of audio data. |
|  `caption` |  \(string\) Caption to display with audio. |

## Methods

### `durations` <a id="durations"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/data_types.py#L592-L594)

```text
@classmethod
durations(
    audio_list
)
```

### `path_is_reference` <a id="path_is_reference"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/data_types.py#L535-L537)

```text
@classmethod
path_is_reference(
    path
)
```

### `resolve_ref` <a id="resolve_ref"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/data_types.py#L608-L614)

```text
resolve_ref()
```

### `sample_rates` <a id="sample_rates"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/data_types.py#L596-L598)

```text
@classmethod
sample_rates(
    audio_list
)
```

| Class Variables |  |
| :--- | :--- |
|  artifact\_type |  \`'audio-file'\` |

