#!/usr/bin/env python
# Mac/Linux SysInfo Script
# by github.com/therealvorteckz
# 
# weechat/irssi - alias sysinfo exec -o sysinfo.py

import psutil
import platform
import cpuinfo
import uptime
import shutil
import socket



# Battery info for Laptops - yes or no
laptop  = 'yes' # yes or no

# Formatting Control Characters / Color Codes / ( do not alter reset )
reset  = '\x0f'
color1  = '14' # bracket close/open = grey
color2  = '04' # color for labels = red

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
cores = psutil.cpu_count(logical=True)
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
    up = ("%d day(s) %d hr(s) %d minute(s) %d sec(s)" % (days, hours, minutes, seconds))
else:
    up = ("%d hr(s) %d minute(s) %d sec(s)" % (hours, minutes, seconds))


# Harddrive Space (Set for Mac HDD Space / Change depedning on your machine)

used_hdd = shutil.disk_usage('/System/Volumes/Data').used
free_hdd = shutil.disk_usage('/System/Volumes/Data').free
total_hdd = shutil.disk_usage('/System/Volumes/Data').total

hdd_free = convertbytes(free_hdd)
hdd_used = convertbytes(used_hdd)
hdd_total = convertbytes(total_hdd)


# Get Machine Local Name
def get_hostname():
    hostname = socket.gethostname()
    return hostname
if laptop == 'yes':
    
    if battery.power_plugged == True:
        print(f"{color("[", color2)}{color("OS:", color1)} {os1} {os2} {os3}{color("]", color2)} {color("[", color2)}{color("Uptime:", color1)} {up}{color("]", color2)} {color("[", color2)}{color("Hostname:", color1)} {get_hostname()}{color("]", color2)} {color("[", color2)}{color("CPU:", color1)} {cpu}{reset} / {cores}x Cores / Load {cpuperc}%{color("]", color2)} {color("[", color2)}{color("Memory:",color1)} {reset}{total} / Used {used}({percent:.2f}%) / Free {free}({100 - percentused}%){color("]", color2)} {color("[", color2)}{color("HDD:", color1)} {hdd_used} / {hdd_free} / {hdd_total}{color("]", color2)} {color("[", color2)}{color("Battery:", color1)} Plugged AC ({battery.percent}%{color("]", color2)}")
    else:
        print(f"{color("[", color2)}{color("OS:", color1)} {os1} {os2} {os3}{color("]", color2)} {color("[", color2)}{color("Uptime:", color1)} {up}{color("]", color2)} {color("[", color2)}{color("Hostname:", color1)} {get_hostname()}{color("]", color2)} {color("[", color2)}{color("CPU:", color1)} {cpu}{reset} / {cores}x Cores / Load {cpuperc}%{color("]", color2)} {color("[", color2)}{color("Memory:",color1)} {reset}{total} / Used {used}({percent:.2f}%) / Free {free}({100 - percentused}%){color("]", color2)} {color("[", color2)}{color("HDD:", color1)} {hdd_used} / {hdd_free} / {hdd_total}{color("]", color2)} {color("[", color2)}{color("Battery:", color1)} {battery.percent}%{color("]", color2)}")
else:
        print(f"{color("[", color2)}{color("OS:", color1)} {os1} {os2} {os3}{color("]", color2)} {color("[", color2)}{color("Uptime:", color1)} {up}{color("]", color2)} {color("[", color2)}{color("Hostname:", color1)} {get_hostname()}{color("]", color2)} {color("[", color2)}{color("CPU:", color1)} {cpu}{reset} / {cores}x Cores / Load {cpuperc}%{color("]", color2)} {color("[", color2)}{color("Memory:",color1)} {reset}{total} / Used {used}({percent:.2f}%) / Free {free}({100 - percentused}%){color("]", color2)} {color("[", color2)}{color("HDD:", color1)} {hdd_used} / {hdd_free} / {hdd_total}{color("]", color2)}")
