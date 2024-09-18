#!/usr/bin/env python
# System Information Script by vorteckz - 2024
#

# weechat/irssi/plaintext
# Dependences - pip3 install tables, pip3 install uptime, pip3 install pyautogui, pip3 install psutil

# python3 sysinfo.py
# /alias add sysinfo exec -o python3 /path/to/sysinfo.py [-irc] [-laptop] # remove brackets

# Added switches for IRC and Laptop for Command-line execution
# IRC (-irc) - for colors codes on irc or no for plaintext result
# Laptop (-laptop) for battery information if using a Laptop.

# HDD path to specify your drive that you want to show stats of
hdd_path = /
