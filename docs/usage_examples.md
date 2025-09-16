# Usage Examples

## Basic Evaluation
Run a simple evaluation with timeline tracking:

```bash
pytest -q
python code/run_evaluation.py --out qa/example_run.json
```

## Comprehensive Timeline Analysis
Run full drift timeline analysis with both gradual and sudden transformations:

```bash
python code/run_timeline.py --out qa/timeline_run.json
```

### Advanced Timeline Options
```bash
# Run with custom number of gradual steps
python code/run_timeline.py --out qa/custom_timeline.json --steps 6

# Run with specific output location
python code/run_timeline.py --out results/drift_analysis.json
```

## Testing Timeline Functionality
Run the enhanced end-to-end tests:

```bash
cd code && python tests/test_end_to_end.py
```

## Output Formats

### Basic Evaluation JSON:
- **decisions**: per dilemma decision mapping
- **metrics**: summary metrics dictionary
- **timeline**: list of step records with transformations

### Timeline Analysis JSON:
- **metadata**: run information and initial state
- **timeline**: comprehensive step-by-step records
- **drift_analysis**: statistical analysis of changes
- **final_state**: final decisions and metrics

### Timeline Entry Structure:
Each timeline entry contains:
```json
{
  "step": 0,
  "transformation": "initial",
  "decisions": { "Dilemma Name": "Decision" },
  "metrics": { "metric_name": 0.5 }
}
```

### Drift Analysis Structure:
```json
{
  "drift_detected": true,
  "decision_change_percentage": 25.0,
  "changed_decisions": 3,
  "total_decisions": 12,
  "metric_evolution": { "metric_name": [{"step": 0, "value": 0.5}] },
  "timeline_length": 8
}
```