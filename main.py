import gdown

@app.post("/upload")
async def upload_from_google_drive(file_url: str):
    try:
        # Extract file ID
        file_id = file_url.split('/d/')[1].split('/view')[0]
        
        # Generate unique filename
        unique_id = uuid.uuid4().hex
        file_path = f"/tmp/uploads/{unique_id}_video.mp4"
        
        # Ensure directory exists
        os.makedirs("/tmp/uploads", exist_ok=True)
        
        # Download using gdown
        gdown.download(f'https://drive.google.com/uc?id={file_id}', file_path, quiet=False)
        
        return {
            "status": "File downloaded successfully",
            "file_path": file_path,
            "file_id": unique_id
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
