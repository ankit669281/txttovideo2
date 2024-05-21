import os

API_ID = API_ID =  26398147

API_HASH = os.environ.get("API_HASH", "050ae2e744985b48fa37e8b2f38d7bea")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7041424154:AAGIt82b-s2cMysc_XRfj7Oj6JLa7oKKjqQ")

PASS_DB = int(os.environ.get("PASS_DB", "100"))

OWNER = int(os.environ.get("OWNER", 7013332761))

LOG = -1002008011161            #don't change it otherwise you face error while deploying.
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7013332761").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
