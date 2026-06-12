# mimi is a nice cat 🐱

# github : https://github.com/MultiRight

# import libraries

import psutil
import sys
import time 

# Enable ANSI escape codes on Windows (not needed on Linux/Mac)
if sys.platform == "win32":
    import os
    os.system("")
    clear = lambda: os.system("cls")
else:
    clear = lambda: print("\033c", end="")

# color variables

color_red = "\033[31m"
color_green = "\033[32m"
color_orange = "\033[33m"
color_light_blue = "\033[94m"
color_reset = "\033[0m"

running = True

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

    # Display consumption data

    if percent_ram >= 80 :
        try :
            print(f"{color_light_blue}======================================RAM monitor======================================{color_reset}")

            print()

            print(f"{color_red}total Ram :{total_rounded}{color_reset}")
            print(f"{color_red}usage Ram : {used_rounded}{color_reset}")
            print(f"{color_red}available Ram : {available_rounded}{color_reset}")
            print(f"{color_red}usage Ram % : {percent_ram}{color_reset}")

            print()

            print(f"{color_light_blue}Extremely High Ram usage{color_reset}")
            print(f"Status : {color_red}Bad{color_reset}")

            time.sleep(0.5)
            clear()

        except KeyboardInterrupt:

            running = False
            print()

            print(f"{color_orange}Thank you for using PyGeoterm!{color_reset}")
            print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")

            
            break

    elif 60 <= percent_ram < 80 :
        try :
            print(f"{color_light_blue}======================================RAM monitor======================================{color_reset}")

            print()

            print(f"{color_orange}total Ram :{total_rounded}{color_reset}")
            print(f"{color_orange}usage Ram : {used_rounded}{color_reset}")
            print(f"{color_orange}available Ram : {available_rounded}{color_reset}")
            print(f"{color_orange}usage Ram % : {percent_ram}{color_reset}")
            print()

            print(f"{color_light_blue}Medium Ram Usage{color_reset}")
            print(f"Status : {color_orange}Good{color_reset}")

            time.sleep(0.5)
            clear()

        except KeyboardInterrupt:
            running = False
            print()

            print(f"{color_orange}Thank you for using PyGeoterm!{color_reset}")
            print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")

            break

    else :
        try :
            print(f"{color_light_blue}======================================RAM monitor======================================{color_reset}")

            print()

            print(f"{color_green}total Ram :{total_rounded}{color_reset}")
            print(f"{color_green}usage Ram : {used_rounded}{color_reset}")
            print(f"{color_green}available Ram : {available_rounded}{color_reset}")
            print(f"{color_green}usage Ram % : {percent_ram}{color_reset}")

            print()

            print(f"{color_light_blue}low ram usage{color_reset}")
            print(f"Status : {color_green}Very Good{color_reset}")

            time.sleep(0.5)
            clear()

        except KeyboardInterrupt:
            running = False
            print()

            print(f"{color_orange}Thank you for using PyGeoterm!{color_reset}")
            print(f"{color_orange}Author : https://github.com/MultiRight{color_reset}")

            break

