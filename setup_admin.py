import os
import django
import sys

# Add project root to path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edukkit_backend.settings')
try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    sys.exit(1)

from authentication.models import User

try:
    if not User.objects.filter(email='admin@edukkit.com').exists():
        User.objects.create_superuser('admin@edukkit.com', 'admin123', name='System Admin')
        print("SUCCESS: Superuser created.")
    else:
        print("INFO: Superuser already exists.")
except Exception as e:
    print(f"ERROR: {e}")
