FROM python:3.9-alpine

# Install system dependencies
RUN apk add --no-cache \
    ffmpeg \
    zip \
    && rm -rf /var/cache/apk/*

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 80

# Startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
