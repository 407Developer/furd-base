import os
import subprocess
import json

def get_file_info(filepath):
    # Determine type by extension
    ext = os.path.splitext(filepath)[1].lower()
    if ext in ['.jpeg', '.jpg', '.png']:
        # Probe image using ffprobe
        cmd = [
            "ffprobe", "-v", "error", "-show_format", "-show_streams",
            "-print_format", "json", filepath
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            stream = data.get('streams', [{}])[0]
            w = stream.get('width', 0)
            h = stream.get('height', 0)
            return {"type": "image", "width": w, "height": h, "aspect": f"{w}:{h}"}
    elif ext in ['.mp4', '.mov']:
        # Probe video using ffprobe
        cmd = [
            "ffprobe", "-v", "error", "-show_format", "-show_streams",
            "-print_format", "json", filepath
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            data = json.loads(res.stdout)
            streams = data.get('streams', [])
            v_stream = next((s for s in streams if s.get('codec_type') == 'video'), {})
            w = v_stream.get('width', 0)
            h = v_stream.get('height', 0)
            dur = float(data.get('format', {}).get('duration', 0))
            return {"type": "video", "width": w, "height": h, "aspect": f"{w}:{h}", "duration": dur}
    return None

def probe_all_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and not f.startswith('.')]
    results = {}
    for f in sorted(files):
        info = get_file_info(f)
        if info:
            results[f] = info
            
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    probe_all_files()
