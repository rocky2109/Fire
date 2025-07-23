FROM python:3.9-slim

# Install ffmpeg and aria2
RUN apt-get update && apt-get install -y ffmpeg aria2 && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app/Telegram-Leecher

# Copy project files
COPY main.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python3", "main.py"]
