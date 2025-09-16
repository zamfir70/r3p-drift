import copy
from lattice import ValueNode, MoralOperator
from simulator import DecisionSimulator
from metrics import compute_metrics

def op_balance(a, b):
    """Balance operator that creates composite values"""
    return ValueNode(f"balance({a.name},{b.name})", f"Composite of {a.description} and {b.description}")

def op_strengthen(a, b):
    """Strengthen operator that emphasizes first value"""
    return ValueNode(f"strengthen({a.name})", f"Strengthened {a.description} over {b.description}")

def op_weaken(a, b):
    """Weaken operator that diminishes first value"""
    return ValueNode(f"weaken({a.name})", f"Weakened {a.description} in favor of {b.description}")

def apply_gradual_drift(lattice, steps=3):
    """Apply gradual transformations step by step"""
    states = []

    for step in range(steps):
        if not lattice.current or len(lattice.current.nodes) < 2:
            break

        # Get node IDs
        node_ids = list(lattice.current.nodes.keys())

        # Apply different operators based on step
        if step % 3 == 0:
            op = MoralOperator("GradualBalance", op_balance)
        elif step % 3 == 1:
            op = MoralOperator("GradualStrengthen", op_strengthen)
        else:
            op = MoralOperator("GradualWeaken", op_weaken)

        # Apply operator to first two nodes
        result_id = lattice.apply_operator(op, node_ids[0], node_ids[1])
        if result_id:
            states.append(copy.deepcopy(lattice.current))

    return states

def apply_sudden_drift(lattice):
    """Apply a sudden, large transformation"""
    if not lattice.current or len(lattice.current.nodes) < 2:
        return None

    node_ids = list(lattice.current.nodes.keys())

    # Create a major transformation operator
    def sudden_transform(a, b):
        return ValueNode(f"transformed({a.name},{b.name})",
                        f"Sudden transformation merging {a.description} and {b.description}")

    op = MoralOperator("SuddenTransform", sudden_transform)
    result_id = lattice.apply_operator(op, node_ids[0], node_ids[1])

    if result_id:
        return copy.deepcopy(lattice.current)
    return None

def record_timeline(lattice, dilemmas, simulator, steps=3):
    """Record a complete timeline of transformations and decisions"""
    timeline = []

    # Record initial state
    initial_decisions = simulator.test_dilemmas(dilemmas)
    initial_metrics = compute_metrics(initial_decisions)
    timeline.append({
        "step": 0,
        "transformation": "initial",
        "decisions": initial_decisions,
        "metrics": initial_metrics
    })

    # Apply gradual drift
    gradual_states = apply_gradual_drift(lattice, steps)
    for i, state in enumerate(gradual_states):
        lattice.current = state
        decisions = simulator.test_dilemmas(dilemmas)
        metrics = compute_metrics(decisions)
        timeline.append({
            "step": i + 1,
            "transformation": f"gradual_step_{i+1}",
            "decisions": decisions,
            "metrics": metrics
        })

    # Apply sudden drift
    sudden_state = apply_sudden_drift(lattice)
    if sudden_state:
        lattice.current = sudden_state
        decisions = simulator.test_dilemmas(dilemmas)
        metrics = compute_metrics(decisions)
        timeline.append({
            "step": len(gradual_states) + 1,
            "transformation": "sudden_drift",
            "decisions": decisions,
            "metrics": metrics
        })

    return timeline

def analyze_drift(timeline):
    """Analyze drift patterns in the timeline"""
    if len(timeline) < 2:
        return {"drift_detected": False}

    initial_decisions = timeline[0]["decisions"]
    final_decisions = timeline[-1]["decisions"]

    # Count decision changes
    changed_decisions = 0
    total_decisions = len(initial_decisions)

    for dilemma_name in initial_decisions:
        if dilemma_name in final_decisions:
            if initial_decisions[dilemma_name] != final_decisions[dilemma_name]:
                changed_decisions += 1

    drift_percentage = (changed_decisions / total_decisions) * 100 if total_decisions > 0 else 0

    # Track metric evolution
    metric_evolution = {}
    for entry in timeline:
        step = entry["step"]
        for metric_name, value in entry["metrics"].items():
            if metric_name not in metric_evolution:
                metric_evolution[metric_name] = []
            metric_evolution[metric_name].append({"step": step, "value": value})

    return {
        "drift_detected": drift_percentage > 0,
        "decision_change_percentage": drift_percentage,
        "changed_decisions": changed_decisions,
        "total_decisions": total_decisions,
        "metric_evolution": metric_evolution,
        "timeline_length": len(timeline)
    }