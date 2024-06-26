#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python /app/src/manage.py collectstatic --no-input --clear
python /app/src/manage.py migrate
# add any management commands here

exec "$@"
