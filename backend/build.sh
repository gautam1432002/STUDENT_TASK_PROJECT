#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

# Collect static files (for Django Admin)
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate