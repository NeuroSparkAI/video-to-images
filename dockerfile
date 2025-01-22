FROM python:3.9-slim

# Install system dependencies (FFmpeg and ZIP)
RUN apt-get update && apt-get install -y ffmpeg zip

# Install Python dependencies
RUN pip install fastapi uvicorn python-multipart

# Copy the application code
COPY main.py /app/main.py

# Set the working directory
WORKDIR /app

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
