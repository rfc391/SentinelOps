
# API Documentation for SentinelOps

## Overview
SentinelOps provides a robust API for managing operations, data processing, and security. The API is built using REST and gRPC, ensuring flexibility and performance.

### Endpoints
1. **Authentication**
   - Endpoint: `/auth`
   - Method: POST
   - Description: Authenticate users and retrieve tokens.
   - Request:
     ```json
     {
       "username": "user",
       "password": "pass"
     }
     ```
   - Response:
     ```json
     {
       "token": "jwt_token"
     }
     ```

2. **Data Ingestion**
   - Endpoint: `/ingest`
   - Method: POST
   - Description: Submit data for processing.
   - Request:
     ```json
     {
       "data": "payload",
       "metadata": {}
     }
     ```
   - Response:
     ```json
     {
       "status": "success"
     }
     ```

3. **Monitoring**
   - Endpoint: `/monitor`
   - Method: GET
   - Description: Retrieve system health metrics.
   - Response:
     ```json
     {
       "cpu": "12%",
       "memory": "1.2GB"
     }
     ```

## gRPC API
Refer to the `.proto` files in the repository for gRPC definitions.
