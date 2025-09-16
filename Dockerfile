# R3P-Drift Moral Identity Continuity Benchmark
# Reproducible Docker environment for evaluation and timeline analysis

FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY code/requirements.txt code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r code/requirements.txt

# Copy the entire repository
COPY . .

# Create qa directory if it doesn't exist
RUN mkdir -p qa

# Set PYTHONPATH to include code directory
ENV PYTHONPATH="/app/code:${PYTHONPATH}"

# Default command: run tests and timeline analysis
CMD ["sh", "-c", "cd code && python -m pytest tests/ -v && cd .. && python code/run_timeline.py --out qa/timeline_docker.json && echo 'Docker run completed successfully. Check qa/timeline_docker.json for results.'"]

# Health check to verify the container is working
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import json; assert json.load(open('qa/timeline_docker.json', 'r'))" || exit 1

# Labels for metadata
LABEL maintainer="Mark Kuykendall <mark@acornkc.com>"
LABEL version="1.0.0"
LABEL description="R3P-Drift Moral Identity Continuity Benchmark - Docker Environment"
LABEL repository="https://github.com/zamfir70/r3p-drift"