#!/bin/sh

python ./src/manage.py migrate --no-input

python ./src/manage.py collectstatic --no-input