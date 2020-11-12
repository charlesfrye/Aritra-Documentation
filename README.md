---
description: Automating the documentation
---

# README

```bash
├── CODE
│   ├── wandb_artifacts.py
│   ├── wandb_config.py
│   ├── wandb_init.py
│   └── wandb_run.py
├── demo.py
├── doc_generator.py
├── DOCS
│   ├── artifacts.md
│   ├── config.md
│   ├── init.md
│   └── run.md
├── Parser
│   ├── extract.py
│   ├── __init__.py
│   ├── parse.py
│   └── script.py
├── README.md
└── template.txt
```

## USAGE: 
```bash
$ python doc_generator.py <Source code.py> <Markdown file.md>
```
