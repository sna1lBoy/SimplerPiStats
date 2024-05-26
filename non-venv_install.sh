#!/bin/bash

# Remove previous installation
if [ -d SimplerPiStats ]; then
  rm -rf SimplerPiStats
fi

# Clone the latest version of the repo
echo Cloning from repo...
git clone https://github.com/sna1lBoy/SimplerPiStats.git SimplerPiStats > /dev/null 2>&1

cd SimplerPiStats || return

# Install dependencies
echo Installing dependencies...
python3 -m pip install flask --break-system-packages  > /dev/null 2>&1
python3 -m pip install waitress --break-system-packages  > /dev/null 2>&1

# Update service file with correct paths
echo Setting up file structure...
sed -i "s|WorkingDirectory=.*|WorkingDirectory=$(pwd)|; s|User=.*|User=$(whoami)|" SimplerPiStats.service

# Remove existing service file and directory
echo Setting up service and relocating files...
if [ -f /lib/systemd/system/SimplerPiStats.service ]; then
  sudo systemctl stop SimplerPiStats
  sudo rm -f /lib/systemd/system/SimplerPiStats.service
fi

sudo cp SimplerPiStats.service /lib/systemd/system/SimplerPiStats.service

# Remove unnecessary local files
echo Cleaning up...
rm install.sh non-venv_install.sh readme.md SimplerPiStats.service
rm -rf .git

# Enable the service
sudo systemctl enable SimplerPiStats
echo Install complete!

# (re)start the service and show logs once install complete
echo Starting service... Please wait...
sudo systemctl daemon-reload
sudo systemctl enable SimplerPiStats
sudo systemctl restart SimplerPiStats && timeout 10 journalctl -u SimplerPiStats --since "0 seconds ago" -f --output=cat