#!/usr/bin/env python3
# IRC/RAW SysInfo Script
# by github.com/therealvorteckz
# 
# weechat/irssi - alias sysinfo exec -o sysinfo.py [-irc] [-laptop]

import psutil
import argparse
import platform
import cpuinfo
import uptime
import shutil
import socket
import pyautogui 

# Formatting Control Characters / Color Codes / ( do not alter reset )

reset  = '\x0f'
color1  = '14' # color for labels = grey
color2  = '03' # color for brackets = red

hdd_path = '/'  # drive path that you want to show the amount of used / free/ total space
 
# IRC Color
def color(msg: str, foreground: str, background: str='') -> str:
    return f'\x03{foreground},{background}{msg}{reset}' if background else f'\x03{foreground}{msg}{reset}'


# Convert Bytes Prefix

def convertbytes(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(KB ** 3)
    TB = float(KB ** 4)
    
    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)
    
# Memory Info

svmem = psutil.virtual_memory()
total = convertbytes(svmem.total)
used = convertbytes(svmem.used)
free = convertbytes(svmem.available)
percent = svmem.percent
percentused = svmem.percent

# CPU Info
cores = psutil.cpu_count(logical=False)
cpufreq = psutil.cpu_freq()
cpuperc = psutil.cpu_percent()
cpu = cpuinfo.get_cpu_info()['brand_raw'] 
os1 = platform.system() 
os2 = platform.release()
os3 = platform.machine()
seconds = uptime.uptime()

# Battery Info for Laptops
minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)
battery = psutil.sensors_battery()

# Uptime Line
if days > 0:
    up = ("%d day(s) %d hr(s) %d minute(s)" % (days, hours, minutes))
else:
    up = ("%d hr(s) %d minute(s)" % (hours, minutes))


# Harddrive Space (Set for Mac HDD Space / Change depedning on your machine)

used_hdd = shutil.disk_usage(hdd_path).used
free_hdd = shutil.disk_usage(hdd_path).free
total_hdd = shutil.disk_usage(hdd_path).total

hdd_free = convertbytes(free_hdd)
hdd_used = convertbytes(used_hdd)
hdd_total = convertbytes(total_hdd)


displayx = pyautogui.size()[0] # getting the width of the screen
displayy  = pyautogui.size()[1] # getting the height of the screen

parser = argparse.ArgumentParser(description="-irc for IRC colors and -laptop if you have a laptop for battery info.") # The arguments without -- are required arguments.
parser.add_argument("-irc", action="store_true", help="IRC True or False for Coloring if True for IRC.")
parser.add_argument("-laptop", action="store_true", help="Laptop switch for battery stats.")
args = parser.parse_args()


# Get Machine Local Name
def get_hostname():
    hostname = socket.gethostname()
    return hostname

if args.irc == True:
    
    if args.laptop == True:
        
        if battery.power_plugged == True:
            print(f"{color('[', color2)}{color('OS:', color1)} {os1} {os2} {os3}{color(']', color2)} {color('[', color2)}{color('Uptime:', color1)} {up}{color(']', color2)} {color('[', color2)}{color('Hostname:', color1)} {get_hostname()}{color(']', color2)} {color('[', color2)}{color('CPU:', color1)} {cpu}{reset} / {cores}x Cores / Load {cpuperc}%{color(']', color2)} {color('[', color2)}{color('Memory:',color1)} {free} / {total}{color(']', color2)} {color('[', color2)}{color('HDD:', color1)} {hdd_used} / {hdd_total}{color(']', color2)} {color('[', color2)}{color('Display:', color1)} {displayx}x{displayy}{color(']', color2)} {color('[', color2)}{color('Battery:', color1)} Plugged AC ({battery.percent:.2f}%){color(']', color2)}")
        else:
            print(f"{color('[', color2)}{color('OS:', color1)} {os1} {os2} {os3}{color(']', color2)} {color('[', color2)}{color('Uptime:', color1)} {up}{color(']', color2)} {color('[', color2)}{color('Hostname:', color1)} {get_hostname()}{color(']', color2)} {color('[', color2)}{color('CPU:', color1)} {cpu}{reset} / {cores}x Cores / Load {cpuperc}%{color(']', color2)} {color('[', color2)}{color('Memory:',color1)} {free} / {total}{color(']', color2)} {color('[', color2)}{color('HDD:', color1)} {hdd_used} / {hdd_total}{color(']', color2)} {color('[', color2)}{color('Display:', color1)} {displayx}x{displayy}{color(']', color2)} {color('[', color2)}{color('Battery:', color1)} {battery.percent:.2f}%{color(']', color2)}")
    else:
            print(f"{color('[', color2)}{color('OS:', color1)} {os1} {os2} {os3}{color(']', color2)} {color('[', color2)}{color('Uptime:', color1)} {up}{color(']', color2)} {color('[', color2)}{color('Hostname:', color1)} {get_hostname()}{color(']', color2)} {color('[', color2)}{color('CPU:', color1)} {cpu}{reset} / {cores}x Cores / Load {cpuperc}%{color(']', color2)} {color('[', color2)}{color('Memory:',color1)} {free} / {total}{color(']', color2)} {color('[', color2)}{color('hDD:', color1)} {hdd_used} / {hdd_total}{color(']', color2)} {color('[', color2)}{color('Display:', color1)} {displayx}x{displayy}{color(']', color2)}")
else:
    if args.laptop == True:
        
        if battery.power_plugged == True:
            print(f"[OS: {os1} {os2} {os3}] [Uptime: {up}] [Hostname: {get_hostname()}] [CPU: {cpu}{reset} / {cores}x Cores / Load {cpuperc}%] [Memory: {reset}{total} / Used {used}({percent:.2f}%) / Free {free}({100 - percentused}%)] [HDD: {hdd_used} / {hdd_free} / {hdd_total}] [Battery: Plugged AC ({battery.percent:.2f}%)]")
        else:
            print(f"[OS: {os1} {os2} {os3}] [Uptime: {up}] [Hostname: {get_hostname()}] [CPU: {cpu}{reset} / {cores}x Cores / Load {cpuperc}%] [Memory: {reset}{total} / Used {used}({percent:.2f}%) / Free {free}({100 - percentused}%)] [HDD: {hdd_used} / {hdd_free} / {hdd_total}] [Battery: {battery.percent:.2f}%]")
    else:
            print(f"[OS: {os1} {os2} {os3}] [Uptime: {up}] [Hostname: {get_hostname()}] [CPU: {cpu}{reset} / {cores}x Cores / Load {cpuperc}%] [Memory: {reset}{total} / Used {used}({percent:.2f}%) / Free {free}({100 - percentused}%)] [HDD: {hdd_used} / {hdd_free} / {hdd_total}]")
 
