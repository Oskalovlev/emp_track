import os

from django.conf import settings

# Логгер
LOG_FORMAT = "%(asctime)s :: %(name)s:%(lineno)s - %(levelname)s - %(message)s"
LOG_FILE = os.path.join(settings.BASE_DIR / "api/logs/file.log")
LOG_DIR = os.path.join(settings.BASE_DIR / "api/logs")
LOG_MESSAGE = "Custom log"
LOG_PASS_FILTER = "password"
