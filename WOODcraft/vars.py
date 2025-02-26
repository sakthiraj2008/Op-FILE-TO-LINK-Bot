# (c) adarsh-goel
# (c) sudor2spr @Opleech
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(('11472991'))
    API_HASH = str(("c78c50d54baf2173e8b3f75c359c0c72"))
    BOT_TOKEN = str(('7754306060:AAGBIJsYxqYe9vUPKuCsg5t7i5xS786ufWk'))
    name = str(('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(('SLEEP_THRESHOLD', '60'))
    WORKERS = int(('WORKERS', '4'))
    BIN_CHANNEL = int(('-1002262171720'))
    PORT = int(('PORT', 8080))
    BIND_ADRESS = str(('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1430742022").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('coder_kakashi_bot'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002262171720")).split())) 
