# Vault Read-only Access Design

This brief documents how Forge consumes artifacts stored in **Vault**. Vault is a versioned repository that stores templates and generation outputs for long term reuse. Forge needs a simple, read-only interface so that the same code can run locally or in service mode without embedding storage logic.

## Rationale

- **Consistency** – Forge should reference artifacts through stable identifiers regardless of storage backend.
- **Safety** – Generation results must be immutable once written to Vault to prevent accidental overwrites.
- **Simplicity** – A small HTTP API keeps dependencies light and works on developer laptops and in containers.

## Proposed Interface

Vault exposes artifacts over HTTP under a configurable base URL. Forge retrieves artifacts using standard `GET` requests:

```
GET /api/v1/artifacts/{id}
```

Responses include metadata and a download URL for the immutable content:

```json
{
  "id": "svc-python-v1",
  "filename": "service-python.zip",
  "sha256": "...",
  "download_url": "/api/v1/artifacts/svc-python-v1/file"
}
```

Artifacts are served as read-only blobs; Vault denies `PUT` or `DELETE` on these paths. Clients may optionally list available artifacts:

```
GET /api/v1/artifacts
```

Forge only needs read access, so authentication (if any) uses a token with download-only permissions.

## Usage in Forge

1. The orchestrator resolves artifact IDs from templates or job records.
2. It constructs the full URL using `VAULT_BASE_URL` (default `http://localhost:8000`).
3. Artifacts are fetched with `GET`. Forge unpacks archives into a working directory but never writes back to Vault.

This design keeps Forge agnostic of the storage implementation while ensuring artifacts remain immutable.
