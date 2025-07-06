# Interface Integration TODO

## 1. Define Interaction Modes
- [x] Document CLI entry points for direct user access.
- [x] Design REST API for service mode and remote callers.
- [ ] Outline event bus semantics for Crucible communication.
- [ ] Specify how Vault exposes read-only artifacts to Forge.

## 2. Build Forge Orchestrator
- [ ] Implement core controller accepting commands from multiple protocols.
- [ ] Provide adapters for CLI, REST, and event bus messages.
- [ ] Support manual (human) control via MCP or similar channels.

## 3. Integrate Repositories
- [ ] Map Crucible events/prompts to Forge generation tasks.
- [ ] Publish generated artifacts to Vault for versioned storage.
- [ ] Fetch schemas or templates from Vault when needed.

## 4. Example Workflows
- [ ] CLI → Orchestrator → Code generation → Vault push.
- [ ] REST call → Orchestrator → Event-driven generation from Crucible prompts.
- [ ] Manual MCP session → Orchestrator → Forge pipeline.

## 5. Documentation & Testing
- [ ] Add diagrams showing Crucible–Forge–Vault data flow.
- [ ] Write integration tests for CLI and REST routes.
- [ ] Update docs with usage examples for each protocol.
