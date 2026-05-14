# Use an official, lightweight Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to ensure Python output is sent straight to terminal
# and prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port that Django runs on
EXPOSE 8000

# The command to start the Django development server
# Binds to 0.0.0.0 so it is accessible from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]