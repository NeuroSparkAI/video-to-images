FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg zip

# Install Python dependencies
RUN pip install fastapi uvicorn python-multipart

# Copy requirements file (create this if it doesn't exist)
COPY requirements.txt /app/requirements.txt

# Install Python packages
RUN pip install -r /app/requirements.txt

# Copy application files
COPY main.py /app/main.py

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 80

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
