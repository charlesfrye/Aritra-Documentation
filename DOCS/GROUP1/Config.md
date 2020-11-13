## Config.persist
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_config#L163-L166)

`def persist(self):`

Calls the callback if it's set











## Config._sanitize_val
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_config#L222-L243)

`def _sanitize_val(self, val):`

Turn all non-builtin values into something safe for YAML











# History
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_history#L14-L64)

`History`

Time series data for Runs. This is essentially a list of dicts where each
dict is a set of summary statistics logged.












## History._update_step
[![Badge](https://img.shields.io/badge/View%20source%20on%20GitHub-black?style=for-the-badge&logo=github)](https://github.com/ariG23498/Aritra-Documentation/blob/master/CODE/Runs/wandb_history#L38-L40)

`def _update_step(self):`

Called after receiving the run from the internal process











