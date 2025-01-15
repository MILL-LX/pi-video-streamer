# Raspberry Pi Video Streamer

Python Video Web Streamer for Raspberry Pi

## Pi Setup

This project was built on a Raspberry Pi Zero 2W.

### Operating System

Buld and boot Raspberry Pi OS Lite (32-bit). We chose 32-bit because we are memory constrained and don't get much benefit from the 64-bit OS.

### System Packages for Python Development

```bash
sudo apt update
sudo apt full-upgrade
sudo apt install \
    git \
    python3 \
    python3-pip 
```

### Add WiFi Networks 

If this will join networks besides the one configured when creatind the SD Card, you can add them with the Text UI for the Network Manager.

```bash
sudo nmtui
```

### [uv](https://github.com/astral-sh/uv) for Python Dependency Management

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Raspberry Pi Camera Python Package

The following installs the picamera2 package including its dependencies such as a compatible version of numpy. The `--no-install-recommends` option installs a slimmer package without some windowing dependencies, as would be suitable on Raspberry Pi OS Lite.

```bash
sudo apt install python3-picamera2 --no-install-recommends
```

## Application Setup

### Clone this project

```bash
git clone https://github.com/MILL-LX/pi-video-streamer.git
```

### Make the Project's Python Virtual Environment

Make sure to include the site packages to gain acces to the Picamera2 that was installed with `apt`

```bash
cd pi-video-streamer/app
uv venv --system-site-packages
uv sync
```
