import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.auth.hashers import make_password

from services.constants.parser import (
    HELP_TEXT_PARSER,
    DELETE_TEXT_PARSER,
    OPTIONS_DELETE,
    DATA_DELETE,
    DATA_DIR,
    DATA_UPLOADED,
    DATA_LOAD_IN_FILE,
)
from api.management.logger import init_logger
from user.models import User


init_logger("parse_users")
logger = logging.getLogger("parse_users")

file_name = "users.csv"


class Command(BaseCommand):

    help = HELP_TEXT_PARSER.format(file_name)

    def add_arguments(self, parser):

        delet = DELETE_TEXT_PARSER.format(file_name)

        parser.add_argument(
            "--delete",
            action="store_true",
            help=delet,
        )

    def handle(self, *args, **options):

        models = [User]

        if options[OPTIONS_DELETE]:
            for model in models:
                model.objects.all().delete()
                logger.info(DATA_DELETE.format(model))

        if not options[OPTIONS_DELETE]:
            for model in models:
                if model.objects.exists():
                    logger.info(DATA_UPLOADED.format(model))
                    return

            with open(
                os.path.join(settings.BASE_DIR / DATA_DIR.format(file_name)),
                encoding="utf-8",
            ) as csv_file:

                reader = csv.reader(csv_file, delimiter=",")
                next(reader)

                for row in reader:
                    User.objects.get_or_create(
                        username=row[0],
                        password=make_password(row[1]),
                        email=row[2],
                        first_name=row[3],
                        last_name=row[4],
                    )
            logger.info(DATA_LOAD_IN_FILE.format(file_name))
