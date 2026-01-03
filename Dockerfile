# PyPitch API Dockerfile
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash pypitch && \
    chown -R pypitch:pypitch /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code as pypitch user
COPY --chown=pypitch:pypitch pypitch/ ./pypitch/
COPY --chown=pypitch:pypitch pyproject.toml .
COPY --chown=pypitch:pypitch README.md .

USER pypitch

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["python", "-m", "uvicorn", "pypitch.serve.api:create_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]