# mimi is a nice cat 

# github : https://github.com/MohssineX
# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>
# SPDX-License-Identifier: GPL-3.0-only

# ram-monitor.py

# import libraries
import sys
import signal
import shutil
import time

# import psutil
try:
    import psutil
except ImportError:
    print("psutil is required. Install it with: pip install psutil")
    sys.exit(1)

# Enable ANSI escape codes on Windows (not needed on Linux/Mac)
if sys.platform == "win32":
    import os
    os.system("")

# color variables
COLOR_YELLOW = "\033[33m"
COLOR_RESET = "\033[0m"

# Exit the application when pressing Ctrl+C.
def handle_interrupt(sig, frame):
    print()
    print(f"{COLOR_YELLOW}Thank you for using ram-monitor!{COLOR_RESET}")
    print(f"{COLOR_YELLOW}Author : https://github.com/MohssineX{COLOR_RESET}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt) 
    
# color variables
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m" 
COLOR_LIGHT_BLUE = "\033[94m" 

# clear variables
CLEAR_LINE = "\033[K"
CLEAR_SCREEN = "\033[H\033[2J\033[3J"

# clear this screen to start the application 
print(CLEAR_SCREEN, end="")

def main():
    last_size = shutil.get_terminal_size()

    # Core
    while True:
        # Extracting data related to the use of Random Access Memory (RAM).
        mem = psutil.virtual_memory()
        total_ram = mem.total
        used_ram = mem.used
        available_ram = mem.available
        percent_ram = mem.percent
        
        # Data rounding
        total_rounded = (round(total_ram / (1024 ** 3) , 2))
        used_rounded = (round(used_ram / (1024 ** 3) , 2))
        available_rounded = (round(available_ram / (1024 ** 3) , 2))
        
        # status ram usage levels
        if percent_ram >= 80:
            color_per = COLOR_RED
            status = "Bad"
            ram_desc = "Extremely High Ram Usage"

        elif 50 <= percent_ram < 80:
            color_per = COLOR_YELLOW
            status = "Normal"
            ram_desc = "Medium Ram Usage"
            
        else: 
            color_per = COLOR_GREEN
            status = "Good"
            ram_desc = "Low Ram Usage"

        current_size = shutil.get_terminal_size()
        if current_size != last_size:
            print(CLEAR_SCREEN, end="")
            last_size = current_size

        # Display consumption data
        print(f"{COLOR_LIGHT_BLUE}{'ram-monitor'.center(68)}{COLOR_RESET}")
        print()
        print("--------------------------------------------------------------------")
        print(f"{color_per}Total Ram : {total_rounded} GB{COLOR_RESET}{CLEAR_LINE}")
        print(f"{color_per}Usage Ram : {used_rounded} GB{COLOR_RESET}{CLEAR_LINE}")
        print(f"{color_per}Available Ram : {available_rounded} GB{COLOR_RESET}{CLEAR_LINE}")
        print(f"{color_per}Usage Ram % : {percent_ram} %{COLOR_RESET}{CLEAR_LINE}")
        print("--------------------------------------------------------------------")

        print()

        print(f"{COLOR_LIGHT_BLUE}{ram_desc}{COLOR_RESET}{CLEAR_LINE}")
        print(f"Status : {color_per}{status}{COLOR_RESET}{CLEAR_LINE}")

        time.sleep(0.5)
        print("\033[H", end="")

if __name__ == "__main__":
    main()
