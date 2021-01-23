#!/bin/bash

# This enables use of gsettings outside ~/.bashrc.
PID=$(pgrep gnome-session| tail -n1)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

# This chooses an image randomly from the folder. 
DIR="/home/ishani/astroPicsScraper/astroPicsScraper/images"
PIC=$(ls $DIR/* | shuf -n1)
echo "pic chosen $PIC"
gsettings set org.gnome.desktop.background picture-uri "file://$PIC"
