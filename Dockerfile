# Use a smaller base image
FROM python:3.9-slim-buster

# Minimize layers and reduce image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    zip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy only requirements first
COPY requirements.txt .

# Install dependencies in a single layer
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 80

# Startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
