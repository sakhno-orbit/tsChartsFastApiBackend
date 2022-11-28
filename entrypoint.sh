#!/bin/bash

if [ "$MONGODB_HOST" = "mongodb" ]
then
    echo "Waiting for mongo..."

    while ! nc -z "$MONGODB_HOST" "$MONGODB_PORT"; do
      sleep 0.3
    done

    echo "Mongo started"
fi

exec "$@"