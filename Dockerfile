# app/Dockerfile

# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Update the package list and install necessary system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \  # Tools for building software (e.g., compilers)
    curl \             # Command-line tool for transferring data with URLs
    software-properties-common \  # Utilities for managing software repositories
    git \              # Version control system
    && rm -rf /var/lib/apt/lists/*  # Clean up cached package lists to reduce image size

# Uncomment the following line to clone a GitHub repository directly into the container
# RUN git clone https://github.com/streamlit/streamlit-example.git .

# Copy all files from the current directory on the host machine to the /app directory in the container
COPY . .

# Install Python dependencies listed in the requirements.txt file
RUN pip3 install -r requirements.txt

# Expose port 80 to allow external access to the application
EXPOSE 80

# Define a health check to verify the container is running and the Streamlit app is healthy
HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

# Set the default command to run the Streamlit app on port 80 and bind it to all network interfaces
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
