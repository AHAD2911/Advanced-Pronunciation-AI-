import subprocess
import os

# FFmpeg path relative to this script
FFMPEG_PATH = os.path.join(os.path.dirname(__file__), "ffmpeg-8.0-essentials_build", "bin", "ffmpeg.exe")

def convert_to_wav(input_file: str) -> str:
    ext = input_file.lower().split(".")[-1]

    if ext == "wav":
        return input_file

    output_file = input_file.rsplit(".", 1)[0] + "_converted.wav"

    print(f"Converting: {input_file} → {output_file}")

    command = [
        FFMPEG_PATH,
        "-y",
        "-i", input_file,
        "-ac", "1",
        "-ar", "16000",
        output_file
    ]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print("FFmpeg Error:", result.stderr)
            raise Exception("FFmpeg conversion failed")

        print("✔ FFmpeg Conversion Successful")
        return output_file

    except Exception as e:
        raise Exception(f"FFmpeg failed: {e}")
