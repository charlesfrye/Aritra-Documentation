# SummaryDict
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_summary.py#L16-L61)

`class SummaryDict(object)`


dict-like which wraps all nested dictionraries in a SummarySubDict,
 and triggers self._root._callback on property changes.










# Summary
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_summary.py#L62-L106)

`class Summary(SummaryDict)`


Summary

The summary statistics are used to track single metrics per model. Calling
wandb.log({'accuracy': 0.9}) will automatically set wandb.summary['accuracy']
to be 0.9 unless the code has changed wandb.summary['accuracy'] manually.

Setting wandb.summary['accuracy'] manually can be useful if you want to keep
a record of the accuracy of the best model while using wandb.log() to keep a
record of the accuracy at every step.

You may want to store evaluation metrics in a runs summary after training has
completed. Summary can handle numpy arrays, pytorch tensors or tensorflow tensors.
When a value is one of these types we persist the entire tensor in a binary file
and store high level metrics in the summary object such as min, mean, variance,
95% percentile, etc.










**Example**

```
wandb.init(config=args)

best_accuracy = 0
for epoch in range(1, args.epochs + 1):
test_loss, test_accuracy = test()
if (test_accuracy > best_accuracy):
    wandb.run.summary["best_accuracy"] = test_accuracy
    best_accuracy = test_accuracy
```

# SummarySubDict
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_summary.py#L107-L121)

`class SummarySubDict(SummaryDict)`


Non-root node of the summary data structure. Contains a path to itself
from the root.










