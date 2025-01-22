from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import uuid
import magic  # For file type detection

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    # Validate file type
    file_content = await file.read()
    file_type = magic.from_buffer(file_content, mime=True)
    
    # Allowed video types
    allowed_types = [
        'video/mp4', 
        'video/mpeg', 
        'video/quicktime', 
        'video/x-msvideo'
    ]
    
    if file_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # File size limit (e.g., 1GB)
    max_size = 1 * 1024 * 1024 * 1024  # 1 GB
    if len(file_content) > max_size:
        raise HTTPException(status_code=413, detail="File too large")
    
    # Generate unique filename
    file_id = uuid.uuid4().hex
    file_path = f"/tmp/uploads/{file_id}_{file.filename}"
    
    # Ensure upload directory exists
    os.makedirs("/tmp/uploads", exist_ok=True)
    
    # Save file
    with open(file_path, "wb") as buffer:
        buffer.write(file_content)
    
    return {
        "filename": file.filename,
        "file_id": file_id,
        "file_type": file_type,
        "size": len(file_content),
        "path": file_path,
        "status": "Video uploaded successfully"
    }
