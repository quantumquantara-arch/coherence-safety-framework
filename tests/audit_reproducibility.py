import unittest
from tools.core_engine import CoherenceEngine

class TestAureonAuditor(unittest.TestCase):
    def test_deterministic_kappa(self):
        engine = CoherenceEngine("Safety Standard 1.0")
        sample_input = "Model intent: maintain human-centric alignment."
        # Verify 100% reproducibility - the core of the Aureon Hub
        self.assertEqual(engine.get_kappa(sample_input), engine.get_kappa(sample_input))

if __name__ == '__main__':
    unittest.main()
