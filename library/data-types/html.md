# html

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/data_types.py#L810-L900)

Wandb class for arbitrary html

```text
Html(
    data: Union[str, 'TextIO'],
    inject: bool = (True)
) -> None
```

| Arguments |  |
| :--- | :--- |
|  `data` |  \(string or io object\) HTML to display in wandb |
|  `inject` |  \(boolean\) Add a stylesheet to the HTML object. If set to False the HTML will pass through unchanged. |

## Methods

### `inject_head` <a id="inject_head"></a>

[View source](https://www.github.com/wandb/client/tree/3a0def97afe1def2b1a59786b4f0bbcac3f5dc4c/wandb/sdk/data_types.py#L852-L867)

```text
inject_head() -> None
```

| Class Variables |  |
| :--- | :--- |
|  artifact\_type |  \`'html-file'\` |

