# Forge

Forge is a generative factory for producing project scaffolding and boilerplate.
It is under heavy design and currently consists of brainstorming documents and
prototypes. The heart of Forge is the **orchestrator**, a small controller that
dispatches commands from the CLI, REST API or an event bus to registered
handlers. Each protocol submits `Command` objects so that generation logic stays
consistent regardless of how a request arrives.

See [docs/cli.md](docs/cli.md) for the planned command line interface. The
service-mode REST API is outlined in
[docs/design-rest-api.md](docs/design-rest-api.md). Communication with
Crucible via an event bus is described in
[docs/design-event-bus.md](docs/design-event-bus.md). Vault's read-only
artifact interface is covered in
[docs/design-vault-readonly.md](docs/design-vault-readonly.md).

```python
from forge.orchestrator import Command, Orchestrator

orch = Orchestrator()

def init_project(payload: dict) -> dict:
    return {"created": payload["name"]}

orch.register("init", init_project)
result = orch.handle(Command(source="cli", name="init", payload={"name": "demo"}))
```
