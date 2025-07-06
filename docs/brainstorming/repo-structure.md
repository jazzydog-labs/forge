# Possible Repository Layout

Below is a proposed layout that separates core modules from extensions and keeps generated code out of version control.

```text
forge/
├── src/               # core library code
│   ├── forge/
│   │   ├── domain/
│   │   ├── app/
│   │   └── infrastructure/
│   └── cli.py
├── agents/            # optional built-in AI agents
├── templates/         # default templates
├── examples/          # sample generation projects
└── docs/
    └── brainstorming/ # design notes (this directory)
```

**Generated** artifacts would live under a separate directory specified by the user (e.g., `generated/`), keeping them isolated from the framework's code.
