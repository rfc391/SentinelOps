
import logging
from typing import Dict, List
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class AlertManager:
    def __init__(self):
        self.logger = logging.getLogger("AlertManager")
        self.alerts: List[Dict] = []
        self.thresholds: Dict[str, float] = {}
        
    def set_threshold(self, metric: str, value: float):
        self.thresholds[metric] = value
        
    def check_threshold(self, metric: str, value: float) -> bool:
        if metric in self.thresholds:
            return value > self.thresholds[metric]
        return False
        
    def create_alert(self, metric: str, value: float, threshold: float):
        alert = {
            "metric": metric,
            "value": value,
            "threshold": threshold,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.alerts.append(alert)
        self.notify_alert(alert)
        
    def notify_alert(self, alert: Dict):
        # Example email notification (configure SMTP settings in production)
        message = f"Alert: {alert['metric']} exceeded threshold. Value: {alert['value']}"
        self.logger.warning(message)
