# Universal API Specification
The Coherence Safety Framework (CSF) provides a model-agnostic REST/Python interface.

### Endpoint: /v1/evaluate/kappa
**Purpose:** Returns the Coherence Scorer ($\kappa$) for a given model output.

**Input:**
- model_output: string
- policy_context: string

**Output:**
- kappa: float (0.0 - 1.0)
- status: "COHERENT" | "DEVIATED (Δϕ)"
