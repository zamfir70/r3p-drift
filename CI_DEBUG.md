# CI Debugging Guide

## Quick Local CI Simulation

### 1. Test the exact CI commands locally:

```bash
# Simulate the CI test job
cd "D:\r3p-drift"
pip install -r code/requirements.txt
mkdir -p qa

cd code
python tests/test_lattice.py
python tests/test_dilemmas.py
python tests/test_simulator.py
python tests/test_timeline.py
python tests/test_end_to_end.py

python run_evaluation.py --out ../qa/example_ci.json
python run_timeline.py --out ../qa/timeline_ci.json
```

### 2. Test Docker build locally:

```bash
# Build the image
docker build -t r3p-drift-debug .

# Run with verbose output
docker run --rm -v $(pwd)/qa:/app/qa r3p-drift-debug

# Check outputs
ls -la qa/
python -c "import json; print(json.load(open('qa/timeline_docker.json'))['metadata'])"
```

### 3. Force a CI trigger:

```bash
# Make a small change to trigger CI
echo "# CI test $(date)" >> README.md
git add README.md
git commit -m "Trigger CI test"
git push origin master
```

## Common CI Failure Patterns:

### **Import Errors:**
- **Symptom**: `ModuleNotFoundError: No module named 'code.tests'`
- **Fix**: Use direct script execution instead of pytest module discovery
- **Test**: `cd code && python tests/test_lattice.py`

### **Path Issues:**
- **Symptom**: `FileNotFoundError: [Errno 2] No such file or directory: 'qa/example_ci.json'`
- **Fix**: Ensure qa directory exists and use relative paths
- **Test**: `mkdir -p qa && cd code && python run_evaluation.py --out ../qa/test.json`

### **Docker Issues:**
- **Symptom**: Container fails or produces no output
- **Fix**: Check Dockerfile CMD and volume mounts
- **Test**: `docker run --rm -it r3p-drift /bin/bash` (interactive debugging)

### **Environment Issues:**
- **Symptom**: Missing dependencies or PYTHONPATH problems
- **Fix**: Set PYTHONPATH and verify requirements.txt
- **Test**: `PYTHONPATH=/path/to/code python run_evaluation.py`

## Real-time CI Monitoring:

1. **GitHub Actions Tab**: https://github.com/zamfir70/r3p-drift/actions
2. **Email Notifications**: Check for GitHub workflow failure emails
3. **Badge Status**: Watch the CI badge in README.md
4. **Artifact Downloads**: Download failed job artifacts for debugging

## Emergency CI Fix Process:

1. **Reproduce locally** using commands above
2. **Fix the issue** in the workflow or code
3. **Test fix locally** before pushing
4. **Push fix** and monitor GitHub Actions
5. **Verify** all three jobs (test, docker-build-and-test, integration-test) pass

## Current CI Workflow Status:

Last known working configuration:
- Direct script execution for tests
- Proper PYTHONPATH setup
- qa directory creation
- Relative path usage for outputs# CI test trigger Tue, Sep 16, 2025  8:48:39 PM
