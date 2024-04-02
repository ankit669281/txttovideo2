import os

API_ID = API_ID = 27464924

API_HASH = os.environ.get("API_HASH", "f28d089001481597f045b70a0daa73e4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7169219459:AAGZ7ZfhJ9O4DwxGOZLhmjqKeoHqUiyimWs")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 6226272085))

LOG = -1002008011161            #don't change it otherwise you face error while deploying.
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6226272085").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
