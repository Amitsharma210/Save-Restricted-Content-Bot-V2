# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26406803"))
API_HASH = getenv("API_HASH", "bee8853d1219e889f6ce5452dc9ef842")
BOT_TOKEN = getenv("BOT_TOKEN", "7289472677:AAEyCzOOGtglSUhJEo_eTG_WdHUWYo9PnY4")
OWNER_ID = int(getenv("OWNER_ID", "7430438132"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://eraon8:d0DiBsv96iEW8JSb@rameshlal.errc5t2.mongodb.net/?retryWrites=true&w=majority&appName=Rameshlal")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002186478269"))
FORCESUB = getenv("FORCESUB", "SBIJuniorAssociateJAClerk")
