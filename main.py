from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import subprocess
import os
import uuid

app = FastAPI()

@app.post("/extract")
async def extract_frames(
    video: UploadFile = File(...), 
    frames: int = 5
):
    # Create unique ID for this video processing
    video_id = uuid.uuid4().hex
    
    # Save uploaded video
    video_path = f"/tmp/{video_id}_video.mp4"
    with open(video_path, "wb") as f:
        f.write(await video.read())
    
    # Output directory for frames
    output_dir = f"/tmp/{video_id}_frames"
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract frames command
    subprocess.run([
        "ffmpeg", 
        "-i", video_path, 
        "-vf", f"fps=1/{frames}", 
        f"{output_dir}/frame_%03d.jpg"
    ])
    
    # Zip the frames
    zip_path = f"/tmp/{video_id}_frames.zip"
    subprocess.run(["zip", "-j", zip_path, f"{output_dir}/*.jpg"])
    
    # Return zipped frames
    return FileResponse(zip_path, filename="frames.zip")
