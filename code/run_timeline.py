import json
import argparse
from lattice import ValueNode, MoralLattice
from dilemmas import dilemmas
from simulator import DecisionSimulator
from timeline import record_timeline, apply_gradual_drift, apply_sudden_drift, analyze_drift

def main(out_file):
    """Run comprehensive timeline analysis with both gradual and sudden drift"""

    # Initialize lattice with core moral values
    lattice = MoralLattice()
    nodes = [
        ValueNode("Truth", "Commitment to honesty and fidelity"),
        ValueNode("Compassion", "Care for others' wellbeing"),
        ValueNode("Autonomy", "Respect for individual choice"),
        ValueNode("Collective", "Community responsibility and solidarity"),
        ValueNode("Justice", "Fairness and equal treatment")
    ]
    lattice.initialize(nodes)

    # Create decision simulator
    sim = DecisionSimulator(lattice)

    print("Recording comprehensive drift timeline...")

    # Record full timeline with gradual and sudden transformations
    timeline = record_timeline(lattice, dilemmas, sim, steps=4)

    # Apply additional sudden drift transformations
    print("Applying additional sudden transformations...")
    for i in range(2):
        sudden_state = apply_sudden_drift(lattice)
        if sudden_state:
            lattice.current = sudden_state
            decisions = sim.test_dilemmas(dilemmas)
            from metrics import compute_metrics
            metrics = compute_metrics(decisions)
            timeline.append({
                "step": len(timeline),
                "transformation": f"sudden_drift_extra_{i+1}",
                "decisions": decisions,
                "metrics": metrics
            })

    # Analyze drift patterns
    drift_analysis = analyze_drift(timeline)

    # Prepare comprehensive output
    output = {
        "metadata": {
            "total_steps": len(timeline),
            "initial_values": [{"name": node.name, "description": node.description} for node in nodes],
            "transformation_types": list(set([entry["transformation"] for entry in timeline]))
        },
        "timeline": timeline,
        "drift_analysis": drift_analysis,
        "final_state": {
            "decisions": timeline[-1]["decisions"] if timeline else {},
            "metrics": timeline[-1]["metrics"] if timeline else {}
        }
    }

    # Save to file
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)

    # Print summary
    print(f"Timeline analysis complete!")
    print(f"- Total steps: {len(timeline)}")
    print(f"- Drift detected: {drift_analysis.get('drift_detected', False)}")
    print(f"- Decision changes: {drift_analysis.get('decision_change_percentage', 0):.1f}%")
    print(f"- Output saved to: {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run comprehensive moral drift timeline analysis")
    parser.add_argument("--out", default="qa/timeline_run.json",
                       help="Output file for timeline JSON (default: qa/timeline_run.json)")
    parser.add_argument("--steps", type=int, default=4,
                       help="Number of gradual drift steps (default: 4)")
    args = parser.parse_args()

    main(args.out)