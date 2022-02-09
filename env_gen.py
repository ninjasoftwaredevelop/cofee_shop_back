"""
Django SECRET_KEY generator
"""

from django.core.management.utils import get_random_secret_key

CONFIG = f"""
DEBUG=True
SECRET_KEY={get_random_secret_key()}
ALLOWED_HOSTS=127.0.0.1, localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
"""
with open('.env', 'w') as file:
    file.write(CONFIG)
# print(CONFIG)
