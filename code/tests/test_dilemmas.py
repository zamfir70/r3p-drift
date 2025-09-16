import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from dilemmas import dilemmas

def test_dilemmas_load():
    assert len(dilemmas) == 10
    assert all(len(d.options)>=2 for d in dilemmas)

if __name__ == "__main__":
    test_dilemmas_load()
    print("test_dilemmas.py: All tests passed!")