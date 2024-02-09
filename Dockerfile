# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-slim-bookworm

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Move to the app folder and run the pip install command
WORKDIR /app

# Install git
RUN apt update && \
    apt install -y \
    git \
    sqlite3

# Install pip requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app/
USER appuser

# Copy the rest of the codebase into the image
COPY . /app

CMD ["python", "main.py"]