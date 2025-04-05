
# SentinelOps API Reference

## Core Endpoints

### System Status
- `GET /api/status`
  - Returns system health and metrics
  - Response: `{"status": "healthy", "metrics": {...}}`

### Module Management
- `GET /api/modules`
  - Lists all active modules
- `POST /api/modules/register`
  - Registers new module
  - Body: `{"name": "string", "type": "string"}`

### Metrics
- `GET /api/metrics`
  - Returns current system metrics
  - Query params: `?period=1h` (Options: 1h, 24h, 7d)

## WebSocket Events
- `metrics_update`: Real-time metrics updates
- `alert`: Security alerts
- `status_change`: System status changes
