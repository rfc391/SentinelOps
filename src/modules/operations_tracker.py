
import logging
from datetime import datetime
from typing import Dict, List

class OperationsTracker:
    def __init__(self, name="Operations Tracker"):
        self.name = name
        self.logger = logging.getLogger(name)
        self.metrics: Dict[str, int] = {
            "operations_count": 0,
            "errors_count": 0,
            "warnings_count": 0
        }
        self.events: List[Dict] = []
        
    def run(self):
        self.logger.info(f"{self.name} starting operation tracking")
        self._track_metrics()
        
    def _track_metrics(self):
        self.metrics["operations_count"] += 1
        self.events.append({
            "timestamp": datetime.now().isoformat(),
            "type": "tracking_started",
            "metrics": self.metrics.copy()
        })
        self.logger.info(f"Current metrics: {self.metrics}")
        
    def get_metrics(self) -> Dict:
        return self.metrics
        
    def get_events(self) -> List[Dict]:
        return self.events
