"""
WSGI config for flagquiz project.
Exposes the WSGI callable as module-level variable named 'application'.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flagquiz.settings')
application = get_wsgi_application()
