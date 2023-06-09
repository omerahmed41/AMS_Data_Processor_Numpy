# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .
COPY requirements_dev.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir -r requirements_dev.txt

# Copy the project code into the container
COPY . .

# Expose a port (if your application requires it)
EXPOSE 8000

# Define the command to run when the container starts
CMD ["python", "app.py"]
