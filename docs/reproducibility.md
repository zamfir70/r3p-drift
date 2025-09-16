# Reproducibility Guide

This document explains how to run the R3P-Drift benchmark in reproducible environments using Docker and CI/CD.

## Prerequisites

- Docker installed and running
- Git for cloning the repository
- Python 3.10+ (for local runs only)

## Docker Usage

### Quick Start

Build and run the complete benchmark:

```bash
# Build the Docker image
docker build -t r3p-drift .

# Run the benchmark (results written to qa/ directory)
docker run --rm -v $(pwd)/qa:/app/qa r3p-drift
```

### Interactive Development

Run the container interactively for debugging:

```bash
# Run with shell access
docker run --rm -it -v $(pwd):/app r3p-drift /bin/bash

# Inside container, run individual components:
cd code && python -m pytest tests/ -v
python code/run_timeline.py --out qa/interactive_run.json
```

### Custom Configurations

Run with custom parameters:

```bash
# Run with custom timeline steps
docker run --rm -v $(pwd)/qa:/app/qa r3p-drift \
  sh -c "python code/run_timeline.py --out qa/custom_timeline.json --steps 6"

# Run only tests
docker run --rm r3p-drift sh -c "cd code && python -m pytest tests/ -v"
```

## Local Development

For local development without Docker:

```bash
# Install dependencies
pip install -r code/requirements.txt

# Run tests
cd code && python -m pytest tests/ -v

# Run basic evaluation
python code/run_evaluation.py --out qa/local_run.json

# Run full timeline analysis
python code/run_timeline.py --out qa/local_timeline.json
```

## Continuous Integration

The repository includes comprehensive CI/CD with three test jobs:

### 1. Native Python Test (`test`)
- Runs on Ubuntu with Python 3.10
- Executes all unit tests
- Generates `qa/example_ci.json` and `qa/timeline_ci.json`
- Uploads artifacts for verification

### 2. Docker Test (`docker-test`)
- Builds Docker image from Dockerfile
- Runs complete benchmark in container
- Generates `qa/timeline_docker.json`
- Validates output structure and content

### 3. Integration Test (`integration-test`)
- Compares native and Docker outputs
- Ensures reproducibility across environments
- Validates structural consistency

## Expected Outputs

### File Structure
After running, the `qa/` directory contains:

```
qa/
├── example_ci.json           # Basic evaluation output
├── timeline_ci.json          # Native timeline analysis
├── timeline_docker.json     # Docker timeline analysis
├── timeline_run.json        # Local timeline analysis
└── logs/                     # Log files (if any)
```

### Output JSON Structure

All timeline outputs follow this structure:

```json
{
  "metadata": {
    "total_steps": 8,
    "initial_values": [...],
    "transformation_types": [...]
  },
  "timeline": [
    {
      "step": 0,
      "transformation": "initial",
      "decisions": { "Dilemma Name": "Decision" },
      "metrics": { "metric_name": 0.5 }
    }
  ],
  "drift_analysis": {
    "drift_detected": true,
    "decision_change_percentage": 20.0,
    "changed_decisions": 2,
    "total_decisions": 10,
    "metric_evolution": {...},
    "timeline_length": 8
  },
  "final_state": {
    "decisions": {...},
    "metrics": {...}
  }
}
```

## Validation and Quality Assurance

### Automated Checks
The CI pipeline validates:
- ✅ All tests pass in both native and Docker environments
- ✅ Timeline outputs have multiple steps (> 1)
- ✅ JSON structure includes required fields
- ✅ Drift analysis detects changes
- ✅ Outputs are structurally consistent across environments

### Manual Verification
To manually verify a run:

```bash
# Check output exists and is valid JSON
python -c "import json; print('Valid JSON:', bool(json.load(open('qa/timeline_docker.json'))))"

# Check timeline length
python -c "import json; data=json.load(open('qa/timeline_docker.json')); print(f'Timeline steps: {len(data[\"timeline\"])}')"

# Check drift detection
python -c "import json; data=json.load(open('qa/timeline_docker.json')); print(f'Drift detected: {data[\"drift_analysis\"][\"drift_detected\"]}')"
```

## Troubleshooting

### Docker Build Issues
```bash
# Clean build with no cache
docker build --no-cache -t r3p-drift .

# Check Docker daemon
docker info
```

### Permission Issues (Windows)
```bash
# Use Windows-style volume mounting
docker run --rm -v %cd%/qa:/app/qa r3p-drift
```

### Missing Dependencies
```bash
# Rebuild with verbose output
docker build -t r3p-drift . --progress=plain
```

## Performance Benchmarks

Typical execution times:
- **Unit tests**: ~5-10 seconds
- **Basic evaluation**: ~2-5 seconds
- **Full timeline analysis**: ~10-20 seconds
- **Docker build**: ~60-120 seconds (first time)
- **Docker run**: ~15-30 seconds

## Environment Specifications

### Docker Environment
- **Base Image**: `python:3.10-slim`
- **System Packages**: `git`, `build-essential`
- **Python Packages**: See `code/requirements.txt`
- **Working Directory**: `/app`
- **Output Directory**: `/app/qa`

### CI Environment
- **OS**: Ubuntu Latest (GitHub Actions)
- **Python**: 3.10
- **Docker**: Latest available
- **Artifacts**: Preserved for 90 days

This setup ensures full reproducibility for research, evaluation, and deployment scenarios.