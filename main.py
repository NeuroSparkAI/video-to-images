from fastapi import FastAPI, HTTPException
import requests
import os
import uuid

app = FastAPI()

@app.post("/upload")
async def upload_from_google_drive(file_url: str = None, file_id: str = None):
    try:
        # Determine file ID
        if file_url:
            file_id = file_url.split('/d/')[1].split('/view')[0]
        
        # Direct download link
        download_url = f"https://drive.google.com/uc?id={file_id}"
        
        # Download file
        response = requests.get(download_url, stream=True)
        
        # Generate unique filename
        file_id = uuid.uuid4().hex
        file_path = f"/tmp/uploads/{file_id}_video.mp4"
        
        # Ensure directory exists
        os.makedirs("/tmp/uploads", exist_ok=True)
        
        # Save file
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return {
            "status": "File downloaded successfully",
            "file_path": file_path,
            "file_id": file_id
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
