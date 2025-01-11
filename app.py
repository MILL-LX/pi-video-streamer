from picamera2 import Picamera2
from libcamera import Transform

# Initialize the camera
camera = Picamera2()
camera.configure(camera.create_video_configuration(transform=Transform(vflip=True), main={"size": (640, 480)}))
camera.set_controls({"AwbEnable": True})  # Enable auto white balance
camera.start()

def main():
    print("Hello from pi-video-streamer!")


if __name__ == "__main__":
    main()
