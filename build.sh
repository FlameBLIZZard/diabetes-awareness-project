#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python packages
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --no-input