#!/bin/bash
echo "Updating system..."
apt-get update && apt-get install -y portaudio19-dev  # PortAudio install karega
pip install -r requirements.txt  # Saari dependencies install karega
