# Usage
For run of the container, `.env` file is required. All ENV are defined in `.env.example`. Container will start, publish message and the stop.

# Commands

## Start container
make up

## Stop container
make down

## Remove container
make remove

## Build of image with no cache
make build

# Logging
All logs are directed to /std/out.

# Example .env File
```
ADMIN=my_admin
PASSWORD=my_password
HOST=my_host
PORT=5672
QUEUE=my_queue
MESSAGE=100
```

# Additional Information
For more information on RabbitMQ and Docker, please refer to the official documentation: \
[RabbitMQ Documentation](https://www.rabbitmq.com/) \
[Docker Documentation](https://docs.docker.com/) \
[Docker Compose Documentation](https://docs.docker.com/compose/)