FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir mysql-connector-python

# Copy application files
COPY . /app

# Run the app (for example, run tests)
CMD ["python", "test.py"]
