FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3.9 python3-pip redis-server

WORKDIR /usr/src/app

COPY . .

# Install Python dependencies for your application
RUN set -ex && pip3 install -r requirements.txt

COPY . .

# Expose the ports for Gunicorn (not exposing for Redis, since we need to access it inside the container)
EXPOSE 8000

# Start Redis server in the background and start Gunicorn as the entrypoint
CMD ["/bin/bash", "-c", "(apachectl -D FOREGROUND &) && redis-server --daemonize yes && gunicorn -c gunicorn_config.py -b0.0.0.0:8000 task_server:app"]
