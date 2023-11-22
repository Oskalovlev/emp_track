from datetime import datetime

# Модели
ZERO = 0
MAX_LENGTH = 150

DATETIME_NOW = datetime.now()


# Юзер-админ
MAIL_LENGTH = 255
MAIL_VALID = r"[^@]+@[^@]+\.[^@]+"
MAIL_ERROR = "{} недопустимый формат эл. почты."

USER_VALID = "Нельзя использовать имя: {}!"
CHAR_VALID = r"^[а-яА-ЯёЁa-zA-Z0-9]+$"
CHAR_VALID_USER = r"^[a-zA-Z0-9]+$"

LENGTH_HELP = f"Максимум {MAX_LENGTH} символов."
