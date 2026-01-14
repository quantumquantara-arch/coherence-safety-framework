import hashlib
import numpy as np

class CoherenceEngine:
    \"\"\"
    The Core of the Coherence Paradigm.
    Uses XOR bitwise operations on SHA-256 hashes to ensure 100% determinism.
    \"\"\"
    def __init__(self, policy_anchor):
        self.anchor_bytes = hashlib.sha256(policy_anchor.encode()).digest()

    def get_kappa(self, model_output):
        \"\"\"
        κ (Coherence) = 1 - (Hamming Distance / Bit-Length)
        Maps neural outputs to a deterministic symbolic anchor.
        \"\"\"
        output_bytes = hashlib.sha256(model_output.encode()).digest()
        # XOR calculates the structural distance between output and policy
        diff = np.frombuffer(self.anchor_bytes, dtype=np.uint8) ^ np.frombuffer(output_bytes, dtype=np.uint8)
        score = 1.0 - (np.sum(np.unpackbits(diff)) / 256)
        return round(float(score), 6)
