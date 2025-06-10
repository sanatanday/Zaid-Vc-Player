## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "BQF8vgIAOf7KJ-EtMVn6HYRr31TI8im6HX_McJxjO4NTO6mwj5rNuOd0-emPoONrbaFI8HBaOK8k3IEWMMou5Dv7dKZnMgAWORItQNZIXkjxY_nRlop5MEx2kHHrOpL8_iLsfOT4UnEfcnjqHWo4OABLN7QyxqxmCcQ_yl8eaa340V_mYvGRIl47ueJvYduKI-ometpAqPzzvMJvEIH3FVoBlwmx-7741-rTVlnDV9VvePGyXyy0aDznS-_lfrdnPvNkQWCnpPcTbvAf3MUTbW_PzQhb0q449VAhlj7GSapz-RvCFN1n_p6FqI7h0b7hdtkN45xgduiaEJp9EPlWLXMyXHRgAAAAHA32nFAA":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "8196327757:AAHF3oHConrcxGGf6cIkiv744E9mymNA1Yc")
BOT_NAME = getenv("BOT_NAME", "Google Music")

API_ID = int(getenv("API_ID", "24952322"))
API_HASH = getenv("API_HASH", "04142256edaf90245ade69bb8bc6870b")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://vipinmusicbot:nKPSXHOE6YNQ9Alp@cluster0.8b6vckw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_NAME = getenv("OWNER_NAME", "Zaid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Advik")
BOT_USERNAME = getenv("BOT_USERNAME", "GooglexMusicBot")
OWNER_ID = getenv("OWNER_ID", "7530834373")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Google Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7880317040").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
