FROM python:3.9-slim

# Install system dependencies (FFmpeg + ZIP)
RUN apt-get update && apt-get install -y ffmpeg zip

# Install Python packages
RUN pip install --no-cache-dir fastapi uvicorn python-multipart

# Copy code
COPY main.py /app/main.py

# Set working directory
WORKDIR /app

# Start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
