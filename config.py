# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "13305226"))
API_HASH = getenv("API_HASH", "8cde2475d6b0cb1162b89ebbac71a95d")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1258310642").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://V:V@cluster0.qywqg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001906470657")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001968355911"))
