from io import BytesIO
import time

from flask import Flask, Response, render_template_string
from picamera2 import Picamera2
from libcamera import Transform


# Initialize the camera
camera = Picamera2()
camera.configure(camera.create_video_configuration(transform=Transform(vflip=True), main={"size": (640, 480)}))
camera.set_controls({"AwbEnable": True})  # Enable auto white balance
camera.start()


# HTML Template for the web page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin: 2;
        }
        .container img {
            max-width: 50%; /* Adjust the size of the images */
            height: auto;
            border: 2px solid #ccc;
            border-radius: 8px;
        }
    </style>
</head>
<body>

    <div class="container">
        <img src="/video_feed" />
        <img src="/video_feed" />
    </div>

</body>
</html>
"""


app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_frames():
    stream = BytesIO()
    while True:
        camera.capture_file(stream, format="jpeg")
        stream.seek(0)
        raw_frame = np.frombuffer(stream.read(), dtype=np.uint8)
        stream.seek(0)
        stream.truncate()

        frame_bytes = raw_frame.tobytes()

        # Yield the frame as part of the MJPEG stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def main():
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    finally:
        camera.stop()


if __name__ == "__main__":
    main()
