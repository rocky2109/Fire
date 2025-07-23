# Copyright 2023 © Xron Trix | https://github.com/Xrontrix10

# ✅ Simplified & Improved Colab Leech Starter Code

API_ID = 0  # Replace with your own
API_HASH = ""
BOT_TOKEN = ""
USER_ID = 0
DUMP_ID = 0

import os
import json
import time
import shutil
import subprocess

# Fix DUMP_ID format if needed
if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    DUMP_ID = int("-100" + str(DUMP_ID))

# Working directory
working_dir = "/app/Telegram-Leecher"
os.makedirs(working_dir, exist_ok=True)

# 🧩 Step 1: Install dependencies (ffmpeg & aria2)
try:
    subprocess.run("apt-get update && apt-get install -y ffmpeg aria2", shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"[ERROR] System dependencies failed: {e}")

# 🧩 Step 2: Clone the repository if not already
if not os.path.exists(os.path.join(working_dir, ".git")):
    try:
        subprocess.run(f"git clone https://github.com/XronTrix10/Telegram-Leecher {working_dir}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to clone Telegram-Leecher repo: {e}")

# 🧩 Step 3: Install Python requirements
requirements_path = os.path.join(working_dir, "requirements.txt")
if os.path.exists(requirements_path):
    try:
        subprocess.run(f"pip install -r {requirements_path}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install Python dependencies: {e}")

# 🧩 Step 4: Save credentials
credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}
with open(os.path.join(working_dir, "credentials.json"), 'w') as f:
    json.dump(credentials, f)

# 🧩 Step 5: Remove previous session (if any)
session_file = os.path.join(working_dir, "my_bot.session")
if os.path.exists(session_file):
    os.remove(session_file)

# ✅ Final Step: Start bot
print("✅ All setup complete. Starting the bot...")
os.chdir(working_dir)
subprocess.run("python3 -m colab_leecher", shell=True)
