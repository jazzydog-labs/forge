# Forge CLI Overview

The Forge command line interface allows developers to drive code generation workflows directly from the terminal. The CLI is designed around a few simple subcommands that mirror common tasks.

## Entry Points

- `forge init` – create a new project directory with a basic configuration file.
- `forge generate` – run generators using the configuration in the current project.
- `forge templates` – list the templates bundled with Forge.
- `forge agents` – list available AI agents that can assist in generation.
- `forge help` – show detailed usage information for any subcommand.

Each command accepts `-h`/`--help` for additional options. The `generate` subcommand will read the project's configuration file (typically `forge.yml`) and produce code artifacts in the designated output directory.

This interface is intentionally minimal so that additional protocols (REST, event bus) can reuse the same orchestrator logic underneath.
