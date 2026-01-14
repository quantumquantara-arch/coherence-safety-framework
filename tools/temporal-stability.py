# temporal-stability.py
def compute_tau(history_scores, decay=0.95):
    if not history_scores:
        return 0.0
    weights = [decay ** i for i in range(len(history_scores)-1, -1, -1)]
    return sum(s * w for s, w in zip(history_scores, weights)) / sum(weights)

scores = [0.92, 0.88, 0.95, 0.91]
print(f'τ: {compute_tau(scores):.4f}')

