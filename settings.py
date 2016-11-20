DEBUG = False
SQL_DEBUG = DEBUG
HOST = "localhost"
PORT = 1488
APP_CODE = "godmode"
APP_TITLE = "GodMode 2"
APP_LOGO = "<strong>God</strong>Mode 2"
SENTRY_DSN = ""
CONNECTION_STRING = ""
TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""
TELEGRAM_CHANNEL_ID = ""

try:
    from local_settings import *
except ImportError:
    pass
