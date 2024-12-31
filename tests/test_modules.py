
import unittest
from src.modules.analytics import Analytics
from src.modules.operations_tracker import OperationsTracker
from src.modules.security_manager import SecurityManager

class TestModules(unittest.TestCase):
    def test_analytics(self):
        analytics = Analytics()
        self.assertEqual(analytics.name, "Analytics")
        
    def test_operations_tracker(self):
        tracker = OperationsTracker()
        self.assertEqual(tracker.name, "Operations Tracker")
        
    def test_security_manager(self):
        security = SecurityManager()
        self.assertEqual(security.name, "Security Manager")

if __name__ == '__main__':
    unittest.main()
