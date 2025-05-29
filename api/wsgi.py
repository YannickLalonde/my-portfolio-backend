import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project's root directory to the Python path
# This is crucial so Django can find your 'portfolio_backend' settings module
# '..' points to my-portfolio-backend/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set the default Django settings module for the 'wsgi' application.
# This assumes your settings are in 'portfolio_backend/settings.py'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_backend.settings')

application = get_wsgi_application()