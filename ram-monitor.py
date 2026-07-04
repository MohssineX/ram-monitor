# mimi is a nice cat 🐱

# github : https://github.com/MohssineX

# Copyright (C) 2026 Mohssine <https://github.com/MohssineX>

# import libraries

import psutil
import sys
import time 
import shutil

# Enable ANSI escape codes on Windows (not needed on Linux/Mac)

if sys.platform == "win32":
    import os
    os.system("")
    
# clear this screen to start the application 

print("\033c", end="")

# color variables

color_red = "\033[31m"
color_green = "\033[32m"
color_yellow = "\033[33m"
color_light_blue = "\033[94m"
color_reset = "\033[0m"

# while status

running = True

last_size = shutil.get_terminal_size()

# Core

while running :

    # Extracting data related to the use of Random Access Memory (RAM).

    memory_telemetry = psutil.virtual_memory()
    total_ram = memory_telemetry.total
    used_ram = memory_telemetry.used
    available_ram = memory_telemetry.available
    percent_ram = memory_telemetry.percent
    
    # Data rounding

    total_rounded = (round(total_ram / (1024 ** 3) , 2))
    used_rounded = (round(used_ram / (1024 ** 3) , 2))
    available_rounded = (round(available_ram / (1024 ** 3) , 2))
    
    # status ram usage levels

    if percent_ram >= 80 :
        color_per = color_red
        status = "Bad       "
        ram_desc = "Extremely High Ram usage "

    elif 60 <= percent_ram < 80 :
        color_per = color_yellow
        status = "Good      "
        ram_desc = "Medium Ram Usage          "
        

    else : 
        color_per = color_green
        status = "Very Good "
        ram_desc = "low ram usage              "

    # Display consumption data

    try :

        current_size = shutil.get_terminal_size()
        if current_size != last_size:
            print("\033c", end="") 
            last_size = current_size
        
        
        print(f"{color_light_blue}                               ram-monitor                               {color_reset}")

        print()
        print("--------------------------------------------------------------------")
        print(f"{color_per}total Ram : {total_rounded} GB    {color_reset}")
        print(f"{color_per}usage Ram : {used_rounded} GB    {color_reset}")
        print(f"{color_per}available Ram : {available_rounded} GB    {color_reset}")
        print(f"{color_per}usage Ram % : {percent_ram} %  {color_reset}")
        print("--------------------------------------------------------------------")

        print()

        print(f"{color_light_blue}{ram_desc}{color_reset}")
        print(f"Status : {color_per}{status}{color_reset}")

        time.sleep(0.5)
        print("\033[H", end="")
        
        
    except KeyboardInterrupt :

            running = False
            print()

            print(f"{color_yellow}Thank you for using ram-monitor!{color_reset}")
            print(f"{color_yellow}Author : https://github.com/MohssineX{color_reset}")
            


