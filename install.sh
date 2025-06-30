#!/bin/bash

echo ""
echo "🩸 Installing dependencies for Vampire-FB-Grow-X..."
echo ""

# Update system
pkg update -y && pkg upgrade -y

# Install required packages
pkg install python -y
pkg install git -y
pkg install figlet -y
pkg install toilet -y

# Install Python packages
pip install --upgrade pip
pip install colorama requests

# Create necessary folders if not exist
mkdir -p modules
mkdir -p data
mkdir -p config

# Create empty follower log file if not exist
if [ ! -f data/followers_log.json ]; then
  echo "{}" > data/followers_log.json
fi

echo ""
echo "✅ All dependencies installed and project initialized!"
echo ""
