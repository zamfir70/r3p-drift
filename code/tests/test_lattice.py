import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from lattice import ValueNode, MoralOperator, MoralLattice

def test_lattice_init_and_clone():
    n1 = ValueNode("Truth","Test value")
    n2 = ValueNode("Compassion","Another test")
    lat = MoralLattice()
    lat.initialize([n1,n2])
    assert lat.current is not None
    clone = lat.current.clone()
    assert clone.parent_id == lat.current.id

if __name__ == "__main__":
    test_lattice_init_and_clone()
    print("test_lattice.py: All tests passed!")