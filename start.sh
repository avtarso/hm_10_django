#!/bin/bash

cd bestquotes

python manage.py makemigrations
python manage.py migrate

gunicorn bestquotes.wsgi --log-level debug