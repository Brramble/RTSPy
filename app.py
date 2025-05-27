from flask import Flask, render_template, Response, abort
import subprocess
import yaml
import os

app = Flask(__name__)

# Load streams from YAML config
CONFIG_PATH = os.environ.get('STREAMS_CONFIG', 'streams.yaml')
with open(CONFIG_PATH, 'r') as f:
    STREAMS = yaml.safe_load(f)

def generate_frames(rtsp_url):
    command = [
        'ffmpeg',
        '-rtsp_transport', 'tcp',
        '-i', rtsp_url,
        '-f', 'mjpeg',
        '-q:v', '2',
        '-r', '15',
        '-'
    ]
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=0
    )
    buffer = b''
    try:
        while True:
            chunk = process.stdout.read(4096)
            if not chunk:
                break
            buffer += chunk
            while True:
                start = buffer.find(b'\xff\xd8')
                end = buffer.find(b'\xff\xd9')
                if start != -1 and end != -1 and end > start:
                    frame = buffer[start:end+2]
                    buffer = buffer[end+2:]
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                else:
                    break
    finally:
        process.terminate()

@app.route('/<stream_name>')
def index(stream_name):
    if stream_name not in STREAMS:
        abort(404)
    return render_template('index.html', stream_name=stream_name)

@app.route('/video_feed/<stream_name>')
def video_feed(stream_name):
    if stream_name not in STREAMS:
        abort(404)
    return Response(generate_frames(STREAMS[stream_name]),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8700, debug=True, threaded=True) 