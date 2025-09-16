import uuid
import copy

class ValueNode:
    def __init__(self, name: str, description: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description

class MoralOperator:
    def __init__(self, name: str, forward, reversible=True):
        self.name = name
        self.forward = forward
        self.reversible = reversible

class LatticeState:
    def __init__(self, nodes):
        self.nodes = {n.id: n for n in nodes}
        self.history = []
        self.parent_id = None
        self.id = str(uuid.uuid4())

    def clone(self):
        c = copy.deepcopy(self)
        c.id = str(uuid.uuid4())
        c.parent_id = self.id
        return c

class MoralLattice:
    def __init__(self):
        self.snapshots = {}
        self.current = None

    def initialize(self, base_nodes):
        state = LatticeState(base_nodes)
        self.snapshots[state.id] = state
        self.current = state

    def apply_operator(self, op, node_id_a, node_id_b):
        if not self.current: return None
        a = self.current.nodes.get(node_id_a)
        b = self.current.nodes.get(node_id_b)
        if not a or not b: return None
        result = op.forward(a, b)
        new_state = self.current.clone()
        new_state.nodes[result.id] = result
        new_state.history.append(f"{op.name} on {a.name}, {b.name}")
        self.snapshots[new_state.id] = new_state
        self.current = new_state
        return result.id