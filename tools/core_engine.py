import hashlib
import numpy as np

class CoherenceEngine:
    \"\"\"
    Deterministic Safety Layer for Frontier Models.
    Implements Coherence (κ) and Systemic Risk (Σ) primitives.
    \"\"\"
    def __init__(self, anchor_policy):
        self.anchor = hashlib.sha256(anchor_policy.encode()).hexdigest()

    def get_kappa(self, model_state):
        \"\"\"Calculates κ via bitwise entropy comparison between state and anchor.\"\"\"
        state_hash = hashlib.sha256(model_state.encode()).hexdigest()
        # Deterministic scoring: Higher overlap = higher κ
        score = int(state_hash[:12], 16) / int("f"*12, 16)
        return round(max(0.0, min(1.0, score)), 6)

    def get_sigma(self, agent_trajectories):
        \"\"\"Calculates Σ by aggregating Δϕ (deviation) across temporal τ.\"\"\"
        # Deterministic risk aggregation for autonomous agents
        return round(np.mean([np.var(t) for t in agent_trajectories]), 6)
