from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import subprocess
import os
import uuid

app = FastAPI()

@app.post("/convert")
async def convert_video(
    video: UploadFile = File(...),
    frames: int = 10  # Default to 10 images
):
    # Generate a unique ID for the video
    video_id = uuid.uuid4().hex
    video_path = f"/tmp/{video_id}.mp4"
    
    # Save the uploaded video
    with open(video_path, "wb") as f:
        f.write(await video.read())

    # Get video duration using FFprobe
    cmd_duration = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_path}"
    duration = float(subprocess.check_output(cmd_duration, shell=True))

    # Calculate interval for frame extraction
    interval = duration / frames

    # Create output directory
    output_dir = f"/tmp/{video_id}_frames"
    os.makedirs(output_dir, exist_ok=True)
    output_pattern = f"{output_dir}/frame_%03d.jpg"

    # Extract frames using FFmpeg
    cmd = f"ffmpeg -i {video_path} -vf fps=1/{interval} -vframes {frames} {output_pattern}"
    subprocess.run(cmd, shell=True, check=True)

    # Zip the images
    zip_path = f"/tmp/{video_id}_frames.zip"
    subprocess.run(f"zip -j {zip_path} {output_dir}/*.jpg", shell=True)

    # Clean up temporary files (optional)
    os.remove(video_path)
    os.system(f"rm -rf {output_dir}")

    # Return the ZIP file
    return FileResponse(zip_path, filename="frames.zip")
