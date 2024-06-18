FROM python:3.10.14-alpine3.20

ENV HOST=$HOST
ENV PORT=$PORT
ENV USER=$USER
ENV PASSWORD=$PASSWORD
ENV QUEUE=$QUEUE
ENV MESSAGE=$MESSAGE

LABEL maintainer "Jakub Noga <jakubnoga95@gmail.com>"

RUN apk update \
    && apk add busybox-extras \
    && pip install pika

CMD ["bash", "-c", "while true; do sleep 60; done"]