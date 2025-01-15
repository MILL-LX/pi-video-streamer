# Systemd Service Installation

This application can start up automatically on reboot of your Raspberry Pi. Use the following commands to install the service, start it, and enable it to start up on reboot:

```bash
cd /home/pi/pi-video-streamer
sudo cp runtime/systemd/pi-video-streamer.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl stop pi-video-streamer.service
sudo systemctl start pi-video-streamer.service
sudo systemctl enable pi-video-streamer.service
```