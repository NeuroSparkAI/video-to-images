FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg zip

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .

# Expose port
EXPOSE 80

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
