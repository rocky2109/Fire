# copyright 2023 © Xron Trix | https://github.com/Xrontrix10


# @title 🖥️ Main Colab Leech Code

# @title Main Code
# @markdown <div><center><img src="https://user-images.githubusercontent.com/125879861/255391401-371f3a64-732d-4954-ac0f-4f093a6605e1.png" height=80></center></div>
# @markdown <center><h4><a href="https://github.com/XronTrix10/Telegram-Leecher/wiki/INSTRUCTIONS">READ</a> How to use</h4></center>

# @markdown <br>

API_ID = 0  # @param {type: "integer"}
API_HASH = ""  # @param {type: "string"}
BOT_TOKEN = ""  # @param {type: "string"}
USER_ID = 0  # @param {type: "integer"}
DUMP_ID = 0  # @param {type: "integer"}


import subprocess, time, json, shutil, os
from IPython.display import clear_output
from threading import Thread

Working = True

banner = '''

 ____   ____.______  ._______  .______       _____._.______  .___  ____   ____
 \\   \\_/   /: __   \\ : .___  \\ :      \\      \\__ _:|: __   \\ : __| \\   \\_/   /
  \\___ ___/ |  \\____|| :   |  ||       |       |  :||  \\____|| : |  \\___ ___/ 
  /   _   \\ |   :  \\ |     :  ||   |   |       |   ||   :  \\ |   |  /   _   \\ 
 /___/ \\___\\|   |___\\ \\_. ___/ |___|   |       |   ||   |___\\|   | /___/ \\___\\
            |___|       :/         |___|       |___||___|    |___|            
                        :                                                     
                                                                              
 
              _____     __     __     __              __          
             / ___/__  / /__ _/ /    / / ___ ___ ____/ /  ___ ____
            / /__/ _ \\/ / _ `/ _ \\  / /_/ -_) -_) __/ _ \\/ -_) __/
            \\___/\\___/_/\\_,_/_.__/ /____|__/\\__/\\__/_//_/\\__/_/   

                                                

'''

print(banner)

import os
import json
import time
import shutil
import subprocess
from threading import Thread
from IPython.display import clear_output

def Loading():
    white = 37
    black = 0
    while Working:
        print("\r" + "░"*white + "▒▒"+ "▓"*black + "▒▒" + "░"*white, end="")
        black = (black + 2) % 75
        white = (white -1) if white != 0 else 37
        time.sleep(0.1)
    clear_output()

# Start loading animation
Working = True
_Thread = Thread(target=Loading, name="Prepare", args=())
_Thread.start()

# Fix DUMP_ID format if needed
if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    DUMP_ID = int("-100" + str(DUMP_ID))

# Create working directory
working_dir = "/app/Telegram-Leecher"
os.makedirs(working_dir, exist_ok=True)

# Install system dependencies
try:
    subprocess.run("apt-get update && apt-get install -y ffmpeg aria2", 
                 shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Failed to install system packages: {e}")

# Clone repository if not exists
if not os.path.exists(os.path.join(working_dir, ".git")):
    try:
        subprocess.run(f"git clone https://github.com/XronTrix10/Telegram-Leecher {working_dir}", 
                      shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")

# Install Python requirements
requirements_path = os.path.join(working_dir, "requirements.txt")
if os.path.exists(requirements_path):
    try:
        subprocess.run(f"pip install -r {requirements_path}", 
                      shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install requirements: {e}")

# Save credentials
credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}

credentials_path = os.path.join(working_dir, "credentials.json")
with open(credentials_path, 'w') as file:
    json.dump(credentials, file)

# Clean up previous session if exists
session_file = os.path.join(working_dir, "my_bot.session")
if os.path.exists(session_file):
    os.remove(session_file)

# Stop loading animation
Working = False
time.sleep(0.5)  # Let animation complete
print("\rStarting Bot....")

#cd /content/Telegram-Leecher/ && python3 -m colab_leecher #type:ignore
