# Orchestrator Core Controller Design

## Rationale
The orchestrator coordinates code generation regardless of whether a request
comes from the CLI, REST API or an event bus. A single controller keeps logic
consistent across these protocols while keeping the surface area small.

## Approach
* Represent each incoming command with a simple dataclass containing `source`,
  `name` and a `payload` dictionary.
* The `Orchestrator` stores a mapping of command names to handler functions.
* Adapters for the CLI, REST or event bus create `Command` objects and pass them
to `Orchestrator.handle()`.
* Handlers are plain callables returning a result dictionary. No protocol
  details are exposed to handlers.

```
CLI/REST/bus -> Command -> Orchestrator -> handler -> result
```

## Alternatives Considered
* Using a command class hierarchy – rejected as over-engineering for the small
  set of actions currently planned.
* Embedding protocol logic in handlers – makes testing and reuse harder and
  complicates future extensions.

## Trade-offs
* The orchestrator is synchronous; async adapters can wrap it if needed.
* Duplicate command names raise an error to avoid accidental overrides.

## Affected Modules
* `forge/orchestrator.py` – new module implementing `Command` and
  `Orchestrator`.
* `tests/test_orchestrator.py` – unit tests for registration and dispatch
  behavior.

