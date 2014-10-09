import site
import os.path
import os
site.addsitedir(os.path.join(os.path.dirname(__file__), '../../lib'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "application.application.settings")


from django.core.wsgi import get_wsgi_application

from djangae.wsgi import DjangaeApplication

application = DjangaeApplication(get_wsgi_application())
