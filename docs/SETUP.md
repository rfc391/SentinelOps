
# Setup Guide for SentinelOps

## Prerequisites
1. Install Docker and Docker Compose.
2. Set up Cloudflare Zero Trust and obtain the necessary API keys.
3. Configure your environment:
   - Redis
   - IPFS Cluster
   - PostgreSQL or Cloudflare D1

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/rfc391/SentinelOps.git
   cd SentinelOps
   ```
2. Configure environment variables:
   ```bash
   cp .env.example .env
   nano .env
   ```
3. Build and run the application:
   ```bash
   docker-compose up --build
   ```

## Configuration
### Cloudflare Integration
Update `cloudflare_config.json`:
```json
{
  "api_key": "your_api_key",
  "zone_id": "your_zone_id"
}
```

### Database Setup
- PostgreSQL:
  ```sql
  CREATE DATABASE sentinelops;
  ```
- Redis:
  Ensure Redis is running on the default port `6379`.
