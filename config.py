import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
URL_A = os.getenv("URL_A")
URL_B = os.getenv("URL_B")
URL_C = os.getenv("URL_C")
START_PIC = os.getenv("START_PIC")
MONGO_URI = os.getenv("MONGO_URI")
ADMINS = list(map(int, os.getenv("ADMINS", "").split()))
