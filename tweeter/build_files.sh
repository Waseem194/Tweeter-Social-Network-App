#!/bin/bash

# Exit on any error
set -e

echo "Starting build process for Django project..."

# 1. Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# 2. Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 3. Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# 4. Run tests (optional)
# echo "Running tests..."
# python manage.py test

echo "Build process completed successfully."
