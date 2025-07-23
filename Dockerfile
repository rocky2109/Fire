FROM python:3.10-slim

# Install required system packages
RUN apt-get update && apt-get install -y \
    ffmpeg \
    aria2 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your project code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start your app (change as needed)
CMD ["python", "main.py"]
