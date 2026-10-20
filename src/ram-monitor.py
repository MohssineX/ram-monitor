# mimi is a nice cat 
# github : https://github.com/MohssineX
# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>
# SPDX-License-Identifier: GPL-3.0-only

# import libraries
import sys
import signal
import shutil
import time

# Enable ANSI escape codes on Windows (not needed on Linux/Mac)
if sys.platform == "win32":
    import os
    os.system("")

# color variables
color_yellow = "\033[33m"
color_reset = "\033[0m"

# Exit the application when pressing Ctrl+C.
def handle_interrupt(sig, frame):
    print()
    print(f"{color_yellow}Thank you for using ram-monitor!{color_reset}")
    print(f"{color_yellow}Author : https://github.com/MohssineX{color_reset}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt) 

# import psutil
try:
    import psutil
except ImportError:
    print("psutil is required. Install it with: pip install psutil")
    sys.exit(1)
    
# clear this screen to start the application 
print("\033c", end="")

# color variables
color_red = "\033[31m"
color_green = "\033[32m"
color_light_blue = "\033[94m"

# clear variables
CLEAR_LINE = "\033[K"

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
            color_per = color_red
            status = "Bad"
            ram_desc = "extremely high ram usage"

        elif 60 <= percent_ram < 80:
            color_per = color_yellow
            status = "Normal"
            ram_desc = "medium ram usage"
            
        else: 
            color_per = color_green
            status = "Very Good"
            ram_desc = "low ram usage"

        # Display consumption data
        current_size = shutil.get_terminal_size()
        if current_size != last_size:
            print("\033c", end="") 
            last_size = current_size
        
        print(f"{color_light_blue}{'ram-monitor'.center(68)}{color_reset}")

        print()
        print("--------------------------------------------------------------------")
        print(f"{color_per}total Ram : {total_rounded} GB{color_reset}{CLEAR_LINE}")
        print(f"{color_per}usage Ram : {used_rounded} GB{color_reset}{CLEAR_LINE}")
        print(f"{color_per}available Ram : {available_rounded} GB{color_reset}{CLEAR_LINE}")
        print(f"{color_per}usage Ram % : {percent_ram} %{color_reset}{CLEAR_LINE}")
        print("--------------------------------------------------------------------")

        print()

        print(f"{color_light_blue}{ram_desc}{color_reset}{CLEAR_LINE}")
        print(f"Status : {color_per}{status}{color_reset}{CLEAR_LINE}")

        time.sleep(0.5)
        print("\033[H", end="")

if __name__ == "__main__":
    main()
