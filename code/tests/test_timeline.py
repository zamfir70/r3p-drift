import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from timeline import apply_gradual_drift, apply_sudden_drift, record_timeline, analyze_drift
from lattice import ValueNode, MoralLattice
from dilemmas import dilemmas
from simulator import DecisionSimulator

def test_timeline_functions():
    """Test timeline tracking functions"""
    # Setup
    nodes = [ValueNode("Truth","Test"),ValueNode("Compassion","Test")]
    lat = MoralLattice()
    lat.initialize(nodes)
    sim = DecisionSimulator(lat)

    # Test gradual drift
    gradual_states = apply_gradual_drift(lat, steps=2)
    assert len(gradual_states) <= 2

    # Test sudden drift
    sudden_state = apply_sudden_drift(lat)
    assert sudden_state is not None

    # Test timeline recording
    timeline = record_timeline(lat, dilemmas[:3], sim, steps=2)
    assert len(timeline) >= 1

    # Test timeline analysis
    analysis = analyze_drift(timeline)
    assert "drift_detected" in analysis
    assert "timeline_length" in analysis

    print("Timeline functions validation passed")

if __name__ == "__main__":
    test_timeline_functions()
    print("test_timeline.py: All tests passed!")