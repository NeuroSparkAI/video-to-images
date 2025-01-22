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

# Copy requirements first
COPY requirements.txt .

# Install dependencies with maximum verbosity
RUN pip install -r requirements.txt --verbose

# Copy entire project
COPY . .

# Verify installations
RUN pip list | grep fastapi
RUN python -c "import fastapi; print(fastapi.__version__)"

# Expose port
EXPOSE 80

# Startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
