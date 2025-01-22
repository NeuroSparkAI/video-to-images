# Build stage
FROM python:3.9-slim AS builder

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg zip

# Set working directory
WORKDIR /app

# Copy requirements
COPY REQUIREMENTS.txt .

# Install dependencies
RUN pip install --no-cache-dir -r REQUIREMENTS.txt

# Final stage
FROM python:3.9-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y ffmpeg zip

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy application files
COPY main.py .

# Expose port
EXPOSE 80

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
