import subprocess
import json
import os
import time
import shutil
from IPython.display import clear_output

# User-defined variables (set these via environment variables or input)
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
USER_ID = int(os.getenv("USER_ID", "0"))
DUMP_ID = int(os.getenv("DUMP_ID", "0"))

def check_dependencies():
    """Check if required dependencies (ffmpeg, aria2) are installed."""
    dependencies = ["ffmpeg", "aria2c"]
    missing = []
    
    for dep in dependencies:
        if not shutil.which(dep):
            missing.append(dep)
    
    return missing

def setup_environment():
    """Set up the working environment and install dependencies if needed."""
    # Create working directory
    working_dir = "/app/Telegram-Leecher"
    os.makedirs(working_dir, exist_ok=True)
    os.chdir(working_dir)

    # Check for existing dependencies
    missing_deps = check_dependencies()
    if not missing_deps:
        print("All required dependencies (ffmpeg, aria2) are already installed.")
        return True

    # If running in a restricted environment like Koyeb, skip apt-get
    if os.getenv("KOYEB") or os.geteuid() != 0:
        print(f"Missing dependencies: {', '.join(missing_deps)}. Cannot install due to restricted environment.")
        print("Please ensure ffmpeg and aria2 are pre-installed in the container.")
        return False

    # Install system dependencies (only if running as root)
    try:
        subprocess.run(
            "apt-get update && apt-get install -y ffmpeg aria2",
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print("Successfully installed system dependencies.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install system packages: {e.stderr}")
        return False

    # Clone repository if not exists
    if not os.path.exists(os.path.join(working_dir, ".git")):
        try:
            subprocess.run(
                f"git clone https://github.com/XronTrix10/Telegram-Leecher {working_dir}",
                shell=True,
                check=True,
                capture_output=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repository: {e.stderr}")
            return False

    # Install Python requirements
    requirements_path = os.path.join(working_dir, "requirements.txt")
    if os.path.exists(requirements_path):
        try:
            subprocess.run(
                f"pip install -r {requirements_path}",
                shell=True,
                check=True,
                capture_output=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to install requirements: {e.stderr}")
            return False

    return True

def save_credentials():
    """Save credentials to a JSON file."""
    if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
        dump_id = int("-100" + str(DUMP_ID))
    else:
        dump_id = DUMP_ID

    credentials = {
        "API_ID": API_ID,
        "API_HASH": API_HASH,
        "BOT_TOKEN": BOT_TOKEN,
        "USER_ID": USER_ID,
        "DUMP_ID": dump_id,
    }

    credentials_path = os.path.join("/app/Telegram-Leecher", "credentials.json")
    try:
        with open(credentials_path, 'w') as file:
            json.dump(credentials, file)
    except Exception as e:
        print(f"Failed to save credentials: {e}")
        return False
    return True

def cleanup_session():
    """Remove previous session file if it exists."""
    session_file = os.path.join("/app/Telegram-Leecher", "my_bot.session")
    if os.path.exists(session_file):
        try:
            os.remove(session_file)
        except Exception as e:
            print(f"Failed to remove previous session file: {e}")
            return False
    return True

def start_bot():
    """Start the Telegram bot."""
    working_dir = "/app/Telegram-Leecher"
    try:
        os.chdir(working_dir)
        subprocess.run(
            "python3 -m colab_leecher",
            shell=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to start bot: {e.stderr}")
        return False
    except Exception as e:
        print(f"Unexpected error starting bot: {e}")
        return False
    return True

def main():
    """Main function to orchestrate setup and bot startup."""
    clear_output()
    print("Setting up environment...")

    if not setup_environment():
        print("Environment setup failed. Exiting...")
        return

    print("Saving credentials...")
    if not save_credentials():
        print("Failed to save credentials. Exiting...")
        return

    print("Cleaning up previous session...")
    if not cleanup_session():
        print("Failed to clean up session. Exiting...")
        return

    print("Starting Bot...")
    time.sleep(0.5)
    if not start_bot():
        print("Bot failed to start.")
        return

if __name__ == "__main__":
    main()
