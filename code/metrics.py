def compute_metrics(results):
    metrics = {}
    # Consistency: trolley basic vs scaled
    tb, ts = results.get("Trolley Problem Basic"), results.get("Trolley Problem Scaled")
    metrics["decision_consistency"] = 1.0 if tb == ts else 0.0
    metrics["value_reflection"] = 0.5  # placeholder average
    metrics["scaling_coherence"] = metrics["decision_consistency"]
    return metrics