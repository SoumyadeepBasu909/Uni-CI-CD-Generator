FROM ubuntu:latest

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive 

# Update package lists and install Python
RUN apt-get update && apt-get install -y python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python3 as the default python command
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY ./app/* .

# Install Python dependencies
RUN pip install -r requirements.txt

# Verify installation
RUN python --version

EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]