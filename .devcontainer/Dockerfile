# Use GitHub's standard Codespaces base image
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system deps required by Manim
RUN apt-get update && apt-get install -y \
    ffmpeg \
    texlive-full \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
