# mcp_demo

This demo provides a simple FastAPI service that demonstrates basic MCP (Model Control Platform) functionality. Models can be registered and listed via HTTP endpoints.

## Running the Service

1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install fastapi uvicorn pydantic
   ```

2. Start the server with:
   ```bash
   uvicorn mcp_service.main:app --reload
   ```

The service exposes two main endpoints:

- `POST /models` – register a new model with `name`, `version`, and optional `description` fields.
- `GET /models` – list all registered models.

## MCP Features (Demo)

- Register models with version information.
- List all registered models in memory.

This is a minimal demonstration and does not persist data between runs.
