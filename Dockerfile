# Dockerfile
FROM jupyter/datascience-notebook:latest
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt