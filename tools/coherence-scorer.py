# coherence-scorer.py
import hashlib
def kappa(data):
    return hashlib.sha256(data.encode()).hexdigest()
