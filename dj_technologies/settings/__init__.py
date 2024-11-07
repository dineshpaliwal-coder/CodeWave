import os
from django.core.exceptions import ImproperlyConfigured

environment = os.getenv("DJANGO_ENV", "dev")

if environment == "dev":
    from .dev import *
elif environment == "prod":
    from .prod import *
else:
    raise ImproperlyConfigured("DJANGO_ENV must be either 'dev' or 'prod'")
