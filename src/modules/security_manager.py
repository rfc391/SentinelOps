
import logging

class SecurityManager:
    def __init__(self, name="Security Manager"):
        self.name = name
        self.logger = logging.getLogger(name)

    def run(self):
        self.logger.info(f"{self.name} starting security monitoring")
        self._monitor_environment()
        
    def _monitor_environment(self):
        self.logger.info("Monitoring operational environment")
