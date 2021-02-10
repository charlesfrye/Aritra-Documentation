# ArtifactVersions

[![](https://www.tensorflow.org/images/GitHub-Mark-32px.png)View source on GitHub](https://www.github.com/wandb/client/tree/master/wandb/apis/public.py#L3151-L3254)

An iterable collection of artifact versions associated with a project and optional filter.

```text
ArtifactVersions(
    client, entity, project, collection_name, type, filters={}, order=None,
    per_page=50
)
```

This is generally used indirectly via the `Api`.artifact\_versions method

| Class Variables |  |
| :--- | :--- |
|  QUERY |  |

