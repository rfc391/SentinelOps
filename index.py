from core.sentinel import Sentinel
from modules.security_manager import SecurityManager
from modules.operations_tracker import OperationsTracker
from modules.analytics import Analytics

def main():
    # Initialize SentinelOps
    sentinel = Sentinel(name="SentinelOps Main Instance")

    # Register modules
    security = SecurityManager()
    tracker = OperationsTracker()
    analytics = Analytics()

    sentinel.register_module(security)
    sentinel.register_module(tracker)
    sentinel.register_module(analytics)

    # Execute all modules
    sentinel.execute()

if __name__ == "__main__":
    main()
