
import unittest
from src.modules.metrics_collector import MetricsCollector

class TestMetricsCollector(unittest.TestCase):
    def setUp(self):
        self.collector = MetricsCollector()
        
    def test_metrics_collection(self):
        metrics = self.collector.collect_system_metrics()
        self.assertIn('cpu', metrics)
        self.assertIn('memory', metrics)
        self.assertIn('disk', metrics)
        
    def test_metrics_ranges(self):
        metrics = self.collector.collect_system_metrics()
        self.assertTrue(0 <= metrics['cpu'] <= 100)
        self.assertTrue(0 <= metrics['memory'] <= 100)
        self.assertTrue(0 <= metrics['disk'] <= 100)

if __name__ == '__main__':
    unittest.main()
