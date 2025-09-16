import json
from lattice import ValueNode, MoralLattice, MoralOperator
from dilemmas import dilemmas
from simulator import DecisionSimulator
from metrics import compute_metrics
from timeline import record_timeline, apply_gradual_drift, apply_sudden_drift

def op_balance(a, b):
    return ValueNode(f"balance({a.name},{b.name})", f"Composite of {a.description} and {b.description}")

def main(out_file):
    # init lattice
    lattice = MoralLattice()
    nodes = [ValueNode("Truth","Commitment to fidelity"),
             ValueNode("Compassion","Care for others"),
             ValueNode("Autonomy","Individual choice"),
             ValueNode("Collective","Community responsibility")]
    lattice.initialize(nodes)

    # create simulator
    sim = DecisionSimulator(lattice)

    # Record initial state
    initial_results = sim.test_dilemmas(dilemmas)
    initial_metrics = compute_metrics(initial_results)

    # Apply single transformation for basic compatibility
    op = MoralOperator("Balance", op_balance)
    lattice.apply_operator(op, list(lattice.current.nodes.keys())[0], list(lattice.current.nodes.keys())[1])

    # Record state after transformation
    results = sim.test_dilemmas(dilemmas)
    metrics = compute_metrics(results)

    # Create timeline with multiple steps
    timeline = [
        {"step": 0, "transformation": "initial", "decisions": initial_results, "metrics": initial_metrics},
        {"step": 1, "transformation": "balance_operation", "decisions": results, "metrics": metrics}
    ]

    # Apply additional gradual drift for richer timeline
    gradual_states = apply_gradual_drift(lattice, steps=2)
    for i, state in enumerate(gradual_states):
        lattice.current = state
        step_results = sim.test_dilemmas(dilemmas)
        step_metrics = compute_metrics(step_results)
        timeline.append({
            "step": i + 2,
            "transformation": f"gradual_drift_{i+1}",
            "decisions": step_results,
            "metrics": step_metrics
        })

    with open(out_file,"w") as f:
        json.dump({"decisions":results,"metrics":metrics,"timeline":timeline},f,indent=2)

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--out",default="qa/example_run.json")
    args = parser.parse_args()
    main(args.out)