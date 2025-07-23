# Copyright 2023 © Xron Trix | https://github.com/Xrontrix10

API_ID = 0  # @param {type: "integer"}
API_HASH = ""  # @param {type: "string"}
BOT_TOKEN = ""  # @param {type: "string"}
USER_ID = 0  # @param {type: "integer"}
DUMP_ID = 0  # @param {type: "integer"}

import os
import json
import shutil
import subprocess

def initialize_bot():
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
        print(f"System packages installation failed: {e}")
        return False
    
    # Clone repository if not exists
    if not os.path.exists(os.path.join(working_dir, ".git")):
        try:
            subprocess.run(f"git clone https://github.com/XronTrix10/Telegram-Leecher {working_dir}", 
                         shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Repository cloning failed: {e}")
            return False
    
    # Install Python requirements
    requirements_path = os.path.join(working_dir, "requirements.txt")
    if os.path.exists(requirements_path):
        try:
            subprocess.run(f"pip install -r {requirements_path}", 
                         shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Requirements installation failed: {e}")
            return False
    
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
    
    return True

if __name__ == "__main__":
    print("Initializing Telegram Leecher...")
    if initialize_bot():
        print("Starting Bot....")
        # Start the main bot process
        try:
            subprocess.run("cd /app/Telegram-Leecher && python3 -m colab_leecher", 
                         shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Bot startup failed: {e}")
    else:
        print("Initialization failed. Please check the error messages above.")
