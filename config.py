# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25067764"))
API_HASH = getenv("API_HASH", "4f8f7336c4f9af5313a0933bc3c76fef")
BOT_TOKEN = getenv("BOT_TOKEN", "7435693597:AAHV7Li7LbARtvGxSUulBjMUe0FNyH1Z7ys")
OWNER_ID = int(getenv("OWNER_ID", "7430438132"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://teepea582:pvqn0j3JtYilZmoM@rajmohan.eu86re3.mongodb.net/?retryWrites=true&w=majority&appName=Rajmohan")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002200268454"))
FORCESUB = getenv("FORCESUB", "SBIJuniorAssociateJAClerk")
