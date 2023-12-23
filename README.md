# Gunicorn and Redis Docker Image

This Docker image is configured to run a Flask application hosted on a Gunicorn server alongside a Redis server. It is based on Ubuntu 22.04.

## Dockerfile Contents

The Dockerfile contains the following steps:

1. Uses the official Ubuntu 22.04 base image.
2. Installs the necessary dependencies, including Redis and Python. Another option would be to just use some base images of either python or redis, but I decided to go with the vanilla up-to-date Ubuntu 22.04 base image.
3. Installs Python dependencies for your application.
4. Exposes ports 8000 for Gunicorn and 6379 for Redis.
5. Starts the Redis server in the background using `CMD`.
6. Sets the entry point to start Gunicorn.

## How to Build the Docker Image

To build the Docker image, run the following command in the directory containing your Dockerfile:

```bash
docker build -t task-server .
```

## How to Run the Application

After building the image, you can run the Gunicorn application alongside the Redis server using the following command:
```bash
docker run -p 8000:8000 -p 6379:6379 task-server
```

## How to interact with the Application

You can interact with the application using the following curl/wget calls.
Please note that the authentication to the app is by using Basic Auth with the username and password encoded in base64.
The only preconfigured existing user in the DB is:
- Username: shmax
- Password: Password12

# Curl
```bash
# Get all Tasks
curl --location 'http://127.0.0.1:8000/api/v1/tasks' \
--header 'Authorization: Basic c2htYXg6UGFzc3dvcmQxMg=='
```

```bash
# Create Task
curl --location 'http://127.0.0.1:8000/api/v1/tasks' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic c2htYXg6UGFzc3dvcmQxMg==' \
--data '{
    "task": "Fix boiler",
    "due_date": "2023-12-31"
    }'
```

```bash
# Get a specific Task
curl --location 'http://127.0.0.1:8000/api/v1/tasks/77d6a7c9-0111-40a2-a731-6a67703fd72d' \
--header 'Authorization: Basic c2htYXg6UGFzc3dvcmQxMg=='
```

```bash
# Edit a specific Task
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/tasks/258bbee9-b180-4703-8c99-0226e34afdb2' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic c2htYXg6UGFzc3dvcmQxMg==' \
--data '{
    "task": "Clean up room and walk dog",
    "due_date": "2023-12-30"
    }'
```

```bash
# Delete a specific Task
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/tasks/fc8af887-fa27-4153-9d8c-bd97029408bc' \
--header 'Authorization: Basic c2htYXg6UGFzc3dvcmQxMg=='
```
