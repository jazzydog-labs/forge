# Forge Event Bus Semantics

This document outlines how Forge communicates with **Crucible** or other tools via an event bus. The goal is to keep messages simple and transport agnostic so that various brokers (Redis, NATS, etc.) can be used.

## Rationale

An event bus enables loosely coupled interactions. Crucible can emit prompts or generation requests without knowing whether Forge is running locally or as a remote service. Forge publishes job status and artifacts back onto the bus for any interested consumer.

## Message Format

- JSON payloads encoded as UTF-8.
- Each message contains a `type` field and a `payload` object.
- Message envelopes may include broker-specific metadata (e.g., routing keys) but are not required by Forge.

Example:

```json
{
  "type": "forge.generate.request",
  "payload": {
    "template": "service-python",
    "parameters": {"name": "demo"}
  }
}
```

## Channels

### `forge.generate.request`
Crucible publishes this to request a new generation job. Forge responds by creating a job and emitting `forge.generate.started` followed by progress events.

### `forge.generate.started`
Published by Forge when it accepts a request. Payload contains the job identifier.

### `forge.generate.progress`
Optional periodic updates with a percentage or stage label. Payload includes the job identifier and progress data.

### `forge.generate.complete`
Emitted when a job finishes successfully. Payload contains the job identifier and references to generated artifacts.

### `forge.generate.error`
Published if a job fails. Payload includes the job identifier and error message.

## Acknowledgement

Brokers that support acknowledgements (e.g., AMQP) should use "at least once" delivery. Forge components must be idempotent so that re-delivery does not corrupt state.

## Future Extensions

- Schema discovery requests (`forge.schema.query`) so Crucible can fetch valid input schemas.
- Streaming logs or agent conversations over a dedicated channel.
