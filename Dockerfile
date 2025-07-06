# Use official Python slim image
FROM python:3.12-slim

# Install Chrome & ChromeDriver
RUN apt-get update && apt-get install -y \
    chromium chromium-driver wget unzip curl gnupg2 fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="${PATH}:/usr/bin/chromium"

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run your script
CMD ["python", "main.py"]
