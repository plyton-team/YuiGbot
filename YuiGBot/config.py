import json
import os


def get_user_list(config, key):
    with open("{}/YuiGBot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    

    API_ID = 1979859  # integer value, dont use ""
    API_HASH = "2d8efd791d4ae887c2411aee30f3542e"
    TOKEN = "1414346382:AAECUQbkrXz_3h9TmQR-c74hYjgwnRB-_Lc"  
    
    OWNER_ID = 1369875901  
    
    OWNER_USERNAME = "@NetSHEEL"
    SUPPORT_CHAT = "Yui_Official"  #
    
    JOIN_LOGGER = (
        -1001396244212
    )  
    
    EVENT_LOGS = (
        -1001409642282
    )  
    

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://uongpvyl:6EroI1svDwm3eAX5A8VG92ar4jdqpaYE@chunee.db.elephantsql.com/uongpvyl"  
    
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "G1YPDBWDmIKKOZ2omw2kIZp1N0y6S6JaL20ELYfSPPKCwlke74If79C3tGSJUZlB"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@Yui_Official"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    ALLOW_CHATS = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

