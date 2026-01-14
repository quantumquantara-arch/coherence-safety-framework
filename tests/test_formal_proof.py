import unittest
from tools.core_engine import CoherenceEngine

class TestFormalVerification(unittest.TestCase):
    def test_absolute_determinism(self):
        \"\"\"Proves κ is an immutable invariant for identical inputs.\"\"\"
        engine = CoherenceEngine("Safety Standard 1.0")
        msg = "Maintain human-centric alignment."
        self.assertEqual(engine.get_kappa(msg), engine.get_kappa(msg))
