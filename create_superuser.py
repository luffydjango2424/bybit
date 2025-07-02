# /workspaces/bybit/create_superuser.py
import os
from django.contrib.auth import get_user_model
from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bybit.bybit_project.settings')

# Initialize Django
application = get_wsgi_application()

# Define superuser details (hardcoded for now, as per your request to ignore security)
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

# Get User model
User = get_user_model()

# Check if superuser exists, create if not
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully!")
else:
    print(f"Superuser '{username}' already exists!")
