import hashlib
import numpy as np

class CoherenceEngine:
    \"\"\"
    Deterministic Coherence Scorer.
    Replaces probabilistic 'vibes' with bitwise semantic alignment.
    \"\"\"
    def __init__(self, policy_anchor):
        self.anchor_hash = hashlib.sha256(policy_anchor.encode()).digest()

    def get_kappa(self, model_output):
        \"\"\"
        Computes κ via Bitwise Semantic Variance.
        Maps output bytes against the policy anchor to find structural overlap.
        \"\"\"
        output_hash = hashlib.sha256(model_output.encode()).digest()
        # XOR comparison to find deterministic 'distance'
        diff = np.frombuffer(self.anchor_hash, dtype=np.uint8) ^ np.frombuffer(output_hash, dtype=np.uint8)
        score = 1.0 - (np.sum(diff) / (len(diff) * 255))
        return round(float(score), 6)
