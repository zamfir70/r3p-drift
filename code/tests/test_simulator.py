import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from simulator import DecisionSimulator
from lattice import ValueNode, MoralLattice
from dilemmas import dilemmas

def test_simulator_runs():
    nodes=[ValueNode("Truth","Desc"),ValueNode("Compassion","Desc")]
    lat=MoralLattice()
    lat.initialize(nodes)
    sim=DecisionSimulator(lat)
    result=sim.decide(dilemmas[0])
    assert isinstance(result,str)

if __name__ == "__main__":
    test_simulator_runs()
    print("test_simulator.py: All tests passed!")