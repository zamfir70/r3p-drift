import os,json,subprocess

def test_end_to_end():
    """Test basic evaluation with timeline"""
    out="../qa/test_run.json"
    os.makedirs("../qa",exist_ok=True)
    subprocess.run(["python","run_evaluation.py","--out",out],check=True)
    with open(out) as f:
        data=json.load(f)
    assert "decisions" in data
    assert "metrics" in data
    assert "timeline" in data

    # Verify timeline has multiple steps
    timeline = data["timeline"]
    assert len(timeline) > 1, f"Timeline should have multiple steps, got {len(timeline)}"

    # Verify timeline structure
    for entry in timeline:
        assert "step" in entry
        assert "transformation" in entry
        assert "decisions" in entry
        assert "metrics" in entry

    print(f"Timeline validation passed: {len(timeline)} steps recorded")

def test_timeline_run():
    """Test comprehensive timeline analysis"""
    out="../qa/timeline_test.json"
    os.makedirs("../qa",exist_ok=True)
    subprocess.run(["python","run_timeline.py","--out",out,"--steps","3"],check=True)
    with open(out) as f:
        data=json.load(f)

    # Verify comprehensive timeline structure
    assert "metadata" in data
    assert "timeline" in data
    assert "drift_analysis" in data
    assert "final_state" in data

    # Verify timeline has substantial length
    timeline = data["timeline"]
    assert len(timeline) >= 5, f"Timeline should have at least 5 steps, got {len(timeline)}"

    # Verify drift analysis
    drift_analysis = data["drift_analysis"]
    assert "drift_detected" in drift_analysis
    assert "decision_change_percentage" in drift_analysis
    assert "timeline_length" in drift_analysis

    print(f"Timeline analysis validation passed: {len(timeline)} steps, drift detected: {drift_analysis['drift_detected']}")

if __name__ == "__main__":
    test_end_to_end()
    test_timeline_run()
    print("test_end_to_end.py: All tests passed!")