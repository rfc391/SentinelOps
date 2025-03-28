from core.sentinel import Sentinel
from modules.security_manager import SecurityManager
from modules.operations_tracker import OperationsTracker
from modules.analytics import Analytics

# Initialize SentinelOps
sentinel = Sentinel(name="SentinelOps Demo")

# Register modules
security = SecurityManager()
tracker = OperationsTracker()
analytics = Analytics()

sentinel.register_module(security)
sentinel.register_module(tracker)
sentinel.register_module(analytics)

# Initialize and run API server
from core.api import SentinelAPI
api = SentinelAPI(sentinel)
api.run(port=5000)
