# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "28640367"))
	API_HASH = os.environ.get("API_HASH", "1155ea430bfb927287488f6ffb1ad892")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6611968744:AAHAkFHafwzUkG3zYhxzKEl0-fyczU5aP5g")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Filestoreses_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002055706453"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "indianshortner.com")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "9aab55003ef433625f6ba71ae73a4eb516824852")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1846472978"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://abcd:abcd@cluster0.vagppfe.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002132282557")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002055706453")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot of Filmyfunda Movies 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Ded eye](https://t.me/OneLuffyD) 
│
├🔸 **movies Updates:** [Movies Channel](https://t.me/Cinema_files_links)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
 I am Super noob Please Support My Hard Work.
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**..
"""
