#!/usr/bin/env bash

# start background tasks 
gunicorn cpapi.wsgi:application &

python manage.py process_tasks