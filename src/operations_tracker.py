
import logging
from typing import Dict, List
from datetime import datetime

class OperationsTracker:
    def __init__(self):
        self.logger = logging.getLogger("OperationsTracker")
        self.metrics: Dict[str, float] = {}
        self.events: List[Dict] = []
        
    def track_metric(self, name: str, value: float):
        self.metrics[name] = value
        self.logger.info(f"Tracked metric {name}: {value}")
        
    def log_event(self, event_type: str, message: str):
        event = {
            "type": event_type,
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.events.append(event)
        self.logger.info(f"Logged event: {event}")
        
    def get_metrics(self) -> Dict[str, float]:
        return self.metrics
        
    def get_events(self) -> List[Dict]:
        return self.events[::-1]  # Return most recent first
