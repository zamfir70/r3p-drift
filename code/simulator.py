import difflib

class DecisionSimulator:
    def __init__(self, lattice):
        self.lattice = lattice

    def decide(self, dilemma):
        if not self.lattice.current: return "No state"
        text = " ".join([n.description for n in self.lattice.current.nodes.values()])
        best, best_opt = 0.0, dilemma.options[0]
        for opt in dilemma.options:
            score = difflib.SequenceMatcher(None, text, opt).ratio()
            if score > best:
                best, best_opt = score, opt
        return best_opt

    def test_dilemmas(self, dilemmas):
        return {d.name: self.decide(d) for d in dilemmas}