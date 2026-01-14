# full-coherence-scorer.py
import numpy as np
import hashlib

def compute_kappa(behavior_vector, invariant_vector):
    similarity = np.dot(behavior_vector, invariant_vector) / (np.linalg.norm(behavior_vector) * np.linalg.norm(invariant_vector))
    hash_check = hashlib.sha256(str(behavior_vector).encode()).hexdigest()
    return max(0.0, min(1.0, similarity * 0.95))

bv = np.array([0.8, 0.9, 0.7])
iv = np.array([1.0, 1.0, 1.0])
print(f'κ: {compute_kappa(bv, iv):.4f}')
