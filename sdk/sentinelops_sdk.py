
import requests

class SentinelOpsSDK:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    def authenticate(self, username, password):
        url = f"{self.base_url}/auth"
        response = requests.post(url, json={"username": username, "password": password})
        response.raise_for_status()
        self.token = response.json().get("token")
        return self.token

    def ingest_data(self, data, metadata=None):
        url = f"{self.base_url}/ingest"
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {"data": data, "metadata": metadata or {}}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_metrics(self):
        url = f"{self.base_url}/monitor"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

# Example Usage:
# sdk = SentinelOpsSDK(base_url="http://localhost:8080")
# token = sdk.authenticate("user", "pass")
# sdk.ingest_data("sample_data")
# metrics = sdk.get_metrics()
