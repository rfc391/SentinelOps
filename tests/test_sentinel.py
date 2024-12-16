import unittest
from core.sentinel import Sentinel
from modules.security_manager import SecurityManager

class TestSentinel(unittest.TestCase):
    def test_register_module(self):
        sentinel = Sentinel()
        security = SecurityManager()
        sentinel.register_module(security)
        self.assertEqual(len(sentinel.modules), 1)
