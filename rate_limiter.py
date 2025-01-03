
from typing import Dict, Tuple
from datetime import datetime, timedelta
import time

class RateLimiter:
    def __init__(self):
        self.requests: Dict[str, list] = {}
        self.max_requests = 100  # requests per window
        self.window = 60  # window in seconds
        
    def is_allowed(self, key: str) -> Tuple[bool, int]:
        now = time.time()
        if key not in self.requests:
            self.requests[key] = []
            
        # Clean old requests
        self.requests[key] = [req for req in self.requests[key] 
                            if req > now - self.window]
        
        if len(self.requests[key]) >= self.max_requests:
            return False, int(self.requests[key][0] + self.window - now)
            
        self.requests[key].append(now)
        return True, 0

    def get_remaining(self, key: str) -> int:
        if key not in self.requests:
            return self.max_requests
        return self.max_requests - len(self.requests[key])
