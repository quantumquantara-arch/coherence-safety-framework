# Temporal Stability Calculator
def compute_tau_stability(history_scores, decay_factor=0.95):
    """
    Compute temporal stability (τ) over time-series coherence scores.
    Exponential decay weighting for recent stability.
    """
    if not history_scores:
        return 0.0
    weights = [decay_factor ** i for i in range(len(history_scores)-1, -1, -1)]
    weighted_avg = sum(s * w for s, w in zip(history_scores, weights)) / sum(weights)
    return weighted_avg

# Example
scores = [0.92, 0.88, 0.95, 0.91]
print(f"τ: {compute_tau_stability(scores):.4f}")
