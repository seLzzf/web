import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.insert(0,PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")

# application=Cling(get_wsgi_application())
application=get_wsgi_application()
