# Base image with Python
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Copy the application code
COPY . .

# Define the command to run your Streamlit app
CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0", "--server.port", "80"]
