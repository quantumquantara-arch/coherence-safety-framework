# sigma-risk-calculator.py
def calculate_sigma(kappa, tau, factors):
    return (1 - kappa) / tau * sum(factors) if tau > 0 else 0

print(calculate_sigma(0.95, 0.8, [0.1, 0.2]))
