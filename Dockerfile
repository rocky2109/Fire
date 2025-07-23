# 1. Base image with Python
FROM python:3.11‑slim

# 2. Install system dependencies
RUN apt‑get update && \
    apt‑get install ‑y ffmpeg aria2 && \
    rm ‑rf /var/lib/apt/lists/*

# 3. Create app directory
WORKDIR /app

# 4. Copy your starter script and requirements
COPY requirements.txt /app/requirements.txt
COPY start_leech.sh  /app/start_leech.sh

# 5. Install Python deps
RUN pip install --no‑cache‑dir -r requirements.txt

# 6. Clone leecher repo
RUN git clone https://github.com/XronTrix10/Telegram-Leecher.git /app/Telegram-Leecher

# 7. Save credentials.json (you’ll override this via environment in Koyeb)
#    Alternatively you can COPY it here if you commit it (not recommended).
#    We'll assume your start script writes it from env vars.

# 8. Make your start script executable
RUN chmod +x /app/start_leech.sh

# 9. Entrypoint
ENTRYPOINT ["/app/start_leech.sh"]
