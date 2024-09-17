import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "26684254"))
API_HASH = os.environ.get("API_HASH", "fc836096a68be3a4fcd7594cb3d9326f")


OWNER_ID = int(os.environ.get("OWNER_ID", "6161189904"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://naruto-uzumaki:naruto-uzumaki@cluster0.fl0bx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002204573377"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002026477147"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get('CUSTOM_CAPTION', '<b>ᴀɴᴏᴛʜᴇʀ ᴀᴅᴠᴇɴᴛᴜʀᴇ, ᴄᴏᴜʀᴛᴇsʏ ᴏғ<a href="https://t.me/anime_mania_0">ᴀɴɪᴍᴇ ᴍᴀɴɪᴀ</a> ♡</b>')

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b>❌Don't Send Me Messages Directly, I'm Only A File Share Bot‼️</b>"

START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention} 👋</b>\n\n<b>I Can Store Private Files In Specified Channel And Other Users Can Access It From A Special Link‼️</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Welcome, {mention} !!</b>\n\n<b>To Continue, Please Subscribe to Our Channel ‼️</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
