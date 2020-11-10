[source](https://github.com/wandb/client/blob/master/wandb/apis/public.py#L172)

```python
Api(self, overrides={})
```

Used for querying the wandb server.

**Examples**:

Most common way to initialize

```python
wandb.Api()
```

**Arguments**:

* `overrides` _dict_ - You can set `base_url` if you are using a wandb server other than https://api.wandb.ai.
You can also set defaults for `entity`, `project`, and `run`.

This is just a fun little thing that I am doing because I prefer print statements and
absurd amount of experimentation to logical reasoning.