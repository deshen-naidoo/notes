# Dockerized Sticky Notes App

This repository contains the Docker configuration for the Sticky Notes Django application.

## Running the Container
To pull and run this image directly from Docker Hub, use the following commands:

1. Pull the image:
`docker pull YOUR_USERNAME/sticky-notes-app:latest`

2. Run the container:
`docker run -dp 8000:8000 YOUR_USERNAME/sticky-notes-app:latest`

The application will be accessible at http://localhost:8000/
