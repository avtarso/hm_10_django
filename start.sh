#!/bin/bash

cd bestquotes

python manage.py makemigrations
python manage.py migrate

python fill.py

gunicorn bestquotes.wsgi:application --bind 0.0.0.0:$PORT --log-level debug