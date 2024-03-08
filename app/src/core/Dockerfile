# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Command to run the Celery worker
CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]
