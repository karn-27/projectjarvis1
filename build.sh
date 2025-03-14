#!/bin/bash
echo "Updating system..."
apt-get update && apt-get install -y portaudio19-dev
pip install sounddevice
