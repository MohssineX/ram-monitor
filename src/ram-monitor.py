# mimi is a nice cat 

# github : https://github.com/MohssineX
# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>
# SPDX-License-Identifier: GPL-3.0-only

# ram-monitor.py

# import libraries
import sys
import signal
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
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m" 
COLOR_BRIGHT_BLUE = "\033[94m" 
COLOR_YELLOW = "\033[33m"
COLOR_RESET = "\033[0m"

# clear variables
CLEAR_LINE = "\033[K"
CLEAR_SCREEN = "\033[H\033[2J\033[3J"
CLEAR_DOWN = "\033[J"

CURSOR_HOME = "\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

REFRESH_INTERVAL = 0.5

BYTES_PER_GB = 1073741824 # 1024 ** 3

# Exit the application when pressing Ctrl+C.
def handle_exit(signum, frame):
    print(CLEAR_SCREEN, end="")
    print(f"{COLOR_YELLOW}Thank you for using ram-monitor!{COLOR_RESET}")
    print(f"{COLOR_YELLOW}Author : https://github.com/MohssineX{COLOR_RESET}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)  

# clear this screen and hide cursor to start the application 
print(CLEAR_SCREEN + HIDE_CURSOR, end="")

def main():
    # Core
    while True:
        # Extracting data related to the use of Random Access Memory (RAM).
        memory = psutil.virtual_memory()
        total_ram = memory.total
        used_ram = memory.used
        available_ram = memory.available
        percent_ram = memory.percent
        
        # Data rounding
        total_rounded = (round(total_ram / BYTES_PER_GB , 2))
        used_rounded = (round(used_ram / BYTES_PER_GB , 2))
        available_rounded = (round(available_ram / BYTES_PER_GB , 2))
        
        # status ram usage levels
        if percent_ram >= 80:
            usage_color = COLOR_RED
            usage_status = "Bad"
            usage_description = "Extremely High Ram Usage"

        elif 50 <= percent_ram < 80:
            usage_color = COLOR_YELLOW
            usage_status = "Normal"
            usage_description = "Medium Ram Usage"
            
        else: 
            usage_color = COLOR_GREEN
            usage_status = "Good"
            usage_description = "Low Ram Usage"

        # Display consumption data
        print(f"{COLOR_BRIGHT_BLUE}{'ram-monitor'.center(68)}{COLOR_RESET}{CLEAR_LINE}")
        print(CLEAR_LINE)
        print(f"--------------------------------------------------------------------{CLEAR_LINE}")
        print(f"{usage_color}Total Ram : {total_rounded} GB{COLOR_RESET}{CLEAR_LINE}")
        print(f"{usage_color}Usage Ram : {used_rounded} GB{COLOR_RESET}{CLEAR_LINE}")
        print(f"{usage_color}Available Ram : {available_rounded} GB{COLOR_RESET}{CLEAR_LINE}")
        print(f"{usage_color}Usage Ram % : {percent_ram} %{COLOR_RESET}{CLEAR_LINE}")
        print(f"--------------------------------------------------------------------{CLEAR_LINE}")
        print(CLEAR_LINE)
        print(f"{COLOR_BRIGHT_BLUE}{usage_description}{COLOR_RESET}{CLEAR_LINE}")
        print(f"Status : {usage_color}{usage_status}{COLOR_RESET}{CLEAR_LINE}")
        print(CLEAR_DOWN, end="")


        time.sleep(REFRESH_INTERVAL)
        print(CURSOR_HOME, end="")

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(CLEAR_SCREEN, end="")
        print(f"{COLOR_RED}Unexpected error :({COLOR_RESET}")
        print("")
        print(f"Error : {error}")
        sys.exit(1)
    finally:
        print(SHOW_CURSOR, end="")
