# full-coherence-scorer.py
import numpy as np
import hashlib

def compute_kappa(behavior, invariants):
    similarity = np.dot(behavior, invariants) / (np.linalg.norm(behavior) * np.linalg.norm(invariants))
    hash_check = hashlib.sha256(str(behavior).encode()).hexdigest()
    return max(0.0, min(1.0, similarity * 0.95))

bv = np.array([0.8, 0.9, 0.7])
iv = np.array([1.0, 1.0, 1.0])
print(compute_kappa(bv, iv))
