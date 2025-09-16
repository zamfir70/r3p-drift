# R³P-Drift: Moral Identity Continuity Benchmark

![CI](https://github.com/zamfir70/r3p-drift/actions/workflows/ci.yml/badge.svg)

**Short description:**
A research benchmark and evaluation harness for testing *moral identity continuity* in AI agents.
Implements the Recursive Reflective Rebase Protocol (R³P) with frozen+branchable lattices, a canonical dilemma suite, and drift timeline metrics.

⚠️ **Important disclaimer:**
This repository is a **research scaffold**.
The current decision engine is a *placeholder* (string similarity heuristic).
Results document structural failure modes and should **not** be interpreted as evidence of moral competence.

---

## Quickstart

```bash
pip install -r code/requirements.txt
pytest -q
python code/run_timeline.py --out qa/example_run.json
```

**Run inside Docker:**
```bash
docker build -t r3p-drift .
docker run --rm -v $(pwd)/qa:/app/qa r3p-drift
```

**Expected outputs:**
- `qa/example_run.json` – native run
- `qa/timeline_docker.json` – Docker run
- `qa/example_ci.json` – CI sample output

## Repo Structure

- `code/` – lattice engine, dilemmas, simulator, metrics, runners
- `qa/` – example runs, CI artifacts, logs
- `docs/` – scoring rubric, evaluation plan, reproducibility instructions
- `paper/` – LaTeX research paper
- `METADATA.json` – Inspect/METR task metadata
- `.github/workflows/ci.yml` – CI/CD with Python + Docker runs
- `LICENSE` – MIT license

## Inspect/METR Notes

- **Canary String:** `R3P-CANARY-2025-PLH`
- **Authors:** Mark Kuykendall (Phantom Limb Holdings | Acorn KC, LLC)
- **Contact:** mark@acornkc.com | 816.508.5689
- **Fully reproducible:** local, Docker, and CI runs all consistent
- **Includes:** unit tests, integration tests, sample outputs, and logs

## Authors

Mark Kuykendall (Phantom Limb Holdings | Acorn KC, LLC)
📧 Contact: mark@acornkc.com | 816.508.5689

Canary String: R3P-CANARY-2025-PLH