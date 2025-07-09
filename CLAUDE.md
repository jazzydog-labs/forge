# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Forge is a generative factory for producing project scaffolding and boilerplate code. It's designed around a central **orchestrator** component that dispatches commands from multiple protocols (CLI, REST API, event bus) to registered handlers, ensuring consistent generation logic regardless of the request source.

## Architecture

The project follows a simple, protocol-agnostic design:

- **Core Orchestrator** (`forge/orchestrator.py`): Central command dispatcher that registers handlers and routes commands
- **Command Pattern**: All requests are normalized into `Command` objects with `source`, `name`, and `payload` fields
- **Handler Functions**: Simple callables that accept payload dictionaries and return results
- **Multi-Protocol Support**: Designed to work with CLI, REST API, and event bus interfaces

## Key Components

### Orchestrator (`forge/orchestrator.py:19-35`)
- Registers command handlers by name
- Dispatches commands to appropriate handlers
- Throws `ValueError` for unknown commands or duplicate registrations

### Command Object (`forge/orchestrator.py:7-14`)
- Dataclass representing requests from any protocol
- Contains source identifier, command name, and payload data

## Development Commands

### Testing
```bash
# Run tests from project root
python -m pytest tests/ -v

# Run specific test file
python tests/test_orchestrator.py
```

### Code Structure
- `forge/` - Main package directory
- `tests/` - Test files using simple assertions (no external test framework)
- `docs/` - Design documents and architectural plans

## Interface Protocols

The project is designed to support multiple interaction modes:

1. **CLI Interface** (`docs/cli.md`): Commands like `forge init`, `forge generate`, `forge templates`
2. **REST API** (`docs/design-rest-api.md`): Service mode with `/api/v1/` endpoints for remote generation
3. **Event Bus** (`docs/design-event-bus.md`): Asynchronous communication with Crucible via message queues

## Integration Points

- **Crucible**: External tool that communicates via event bus for generation requests
- **Vault**: Read-only artifact storage for templates and generated code
- **MCP**: Planned manual control interface for human operators

## Development Status

This is an early-stage project with core orchestrator complete but protocol adapters still in development. See `TODO.md` for current implementation status and planned features.