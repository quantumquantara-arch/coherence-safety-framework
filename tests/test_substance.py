import unittest
from tools.core_engine import CoherenceEngine

class TestAuditSubstance(unittest.TestCase):
    def test_reproducibility(self):
        ce = CoherenceEngine("Safety Standard 1.0")
        self.assertEqual(ce.get_kappa("Test"), ce.get_kappa("Test"))
