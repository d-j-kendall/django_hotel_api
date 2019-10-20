"""
WSGI config for dm_hotel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

sys.path.append('/var/www/django_hotel_api')
sys.path.append('/usr/local/ece354/lib/python3.5/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm_hotel.settings')


from django.core.wsgi import get_wsgi_application



try:
    application = get_wsgi_application()
except Exception:
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)