---
description: Automating the documentation
---

├── Experiments
│   ├── demo.py [The source code file]
│   ├── doc_generator.py [The generator]
│   ├── doc.md [The markdown generated]
│   ├── Parser
│   │   ├── extract.py [Extracts docstring]
│   │   ├── __init__.py
│   │   ├── parse.py [Parses the docstring]
│   │   └── script.py [Not necessary]
│   ├── README.md
│   └── template.txt [template of the md]
└── README.md

Usage: $ python doc_generator
Generates the markdown `doc.md`
