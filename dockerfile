FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    zip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip install --upgrade pip

# Direct pip installation with verbose output
RUN pip install --verbose fastapi uvicorn python-multipart

# Copy project files
COPY . .

# Verify installation
RUN pip list | grep fastapi
RUN python -c "import fastapi; print(fastapi.__version__)"

# Expose port
EXPOSE 80

# Startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
