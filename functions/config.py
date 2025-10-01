from decouple import config

class Var:
    # Version

    __version__ = "v0.1@stable.july"

    # Telegram Credentials

    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    SESSION = config("SESSION", default=None)

    # Database Credentials

    MONGO_SRV = config("MONGO_SRV", default=None)

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=0, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", cast=int)
    FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", default=0, cast=int)
    OWNER = config("OWNER", default=0, cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://fayoanime.web.app/as/anishare.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="23")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    LOG_ON_MAIN = config("LOG_ON_MAIN", default=False, cast=bool)
    FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="", cast=str)

    # Dev Configs

    DEV_MODE = config("DEV_MODE", default=False, cast=bool)
