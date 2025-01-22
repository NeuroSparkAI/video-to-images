FROM python:3.9-slim
RUN apt-get update && apt-get install -y ffmpeg zip
RUN pip install fastapi uvicorn python-multipart
COPY main.py /app/main.py
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
