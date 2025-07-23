FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your project code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start your app (change as needed)
CMD ["python", "main.py"]
