# Jupyter Lab Development Server

This project sets up a Jupyter Lab server in a Docker container for development purposes. It uses
the `jupyter/datascience-notebook:latest` Docker image as a base and installs additional Python packages from
a `requirements.txt` file.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.

## Building the Docker Image

To build the Docker image, run the following command in the project directory:

```bash
docker-compose build
```

This command builds a new Docker image based on the Dockerfile in the project directory. It installs the Python packages
listed in the requirements.txt file.  
Running the Jupyter Lab Server
To start the Jupyter Lab server, run the following command in the project directory:

```bash
docker-compose up
```

This command starts a Docker container based on the image built in the previous step. It maps port 8888 in the Docker
container to port 8888 on your local machine. The Jupyter Lab server runs at http://localhost:8888. You can access it in
your web browser.  
Stopping the Jupyter Lab Server
To stop the Jupyter Lab server, press Ctrl+C in the terminal where you ran docker-compose up.

### Data and Notebooks

The docker-compose.yml file maps the local ./notebooks directory to /opt/app/notebooks in the Docker container and the
local ./data directory to /opt/app/data in the Docker container. You can add your Jupyter notebooks to the ./notebooks
directory and your data files to the ./data directory. They will be accessible in the Jupyter Lab server.

### Customizing the Python Environment

To add more Python packages to the Jupyter Lab server, add them to the requirements.txt file and rebuild the Docker
image with docker-compose build.