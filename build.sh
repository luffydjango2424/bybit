#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply migrations
python manage.py migrate

# Create superuser using the new script 
python create_superuser.py



# Create superuser if it doesn't exist
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
      if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists(): \
          User.objects.create_superuser(username=os.getenv('DJANGO_SUPERUSER_USERNAME'), \
          email=os.getenv('DJANGO_SUPERUSER_EMAIL'), password=os.getenv('DJANGO_SUPERUSER_PASSWORD'))" | python manage.py shell
