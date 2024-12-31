
import time
from typing import Dict, List
import psutil

class MetricsCollector:
    def __init__(self, name: str = "Metrics Collector"):
        self.name = name
        self.metrics: Dict[str, List[float]] = {
            "cpu": [],
            "memory": [],
            "disk": []
        }
        
    def run(self) -> None:
        self.collect_system_metrics()
        
    def collect_system_metrics(self) -> Dict:
        metrics = {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
        for key, value in metrics.items():
            self.metrics[key].append(value)
        return metrics
