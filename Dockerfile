FROM python:3.10-slim

# Install git
RUN apt-get update && apt-get install -y git \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
