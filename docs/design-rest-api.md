# Forge REST API Design

This document outlines the REST interface for running Forge in **service mode**. The API allows remote callers to trigger generation workflows and inspect available templates.

## Rationale

Providing a small REST layer lets external tools drive Forge without relying on
the CLI. It reuses the orchestrator so that behavior stays consistent across
protocols.

## Trade-offs

- Adds an HTTP server dependency when used.
- Network latency makes synchronous generation less desirable for large jobs;
  an asynchronous job model keeps the API responsive.

## Principles

- **Simple HTTP semantics** – JSON request/response, predictable status codes.
- **Same orchestration core** – the REST service uses the same command handlers as the CLI.
- **Read-only by default** – generation results are immutable once produced.

## Base URL

All endpoints are served under `/api/v1/`.

## Endpoints

### `GET /health`
Returns `200 OK` when the service is running.

### `POST /generate`
Submit a generation request.

```json
{
  "template": "service-python",
  "parameters": {"name": "demo"}
}
```

Response contains a job identifier and initial status.

### `GET /jobs/{id}`
Retrieve the status and resulting artifacts for a generation job.

### `GET /templates`
List available templates with basic metadata.

### `GET /templates/{name}`
Return details for a single template, such as required parameters.

## Error Handling

- `400 Bad Request` for malformed input.
- `404 Not Found` when a job or template does not exist.
- `5xx` codes for server errors.

## Future Extensions

- WebSocket or SSE streaming for real-time job updates.
- Authentication via API tokens when deployed in multi-user environments.

