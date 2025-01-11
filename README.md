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

### [uv](https://github.com/astral-sh/uv) for Python Dependency Management

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Raspberry Pi Camera Python Package

```bash
sudo apt install -y python3-picamera2
```

## Application Setup

### Clone this project

```bash
git clone https://github.com/MILL-LX/pi-video-streamer.git
```
