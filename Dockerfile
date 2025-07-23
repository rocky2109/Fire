FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    git \
    build-essential \
    ffmpeg \  # Required for moviepy and yt-dlp
    libgl1 \  # Required for OpenCV
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Verify critical installations
RUN python -c "import cv2, moviepy, GPUtil, pyrofork; print('Dependencies verified')"

# Clean up
RUN apt-get remove -y gcc python3-dev build-essential && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3", "main.py"]
