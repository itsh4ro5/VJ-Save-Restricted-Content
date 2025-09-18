import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8062527372:AAGHyB7Y4d0mFl41Anry1Y0wvzcmA5tkSzw")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29482568"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cd9ef7ed69ef8cbec112f71d99471080")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1655270771"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://itsh4r03_db_user:hJuj71D4YlhQ8Y3H@forward.uttldww.mongodb.net/?retryWrites=true&w=majority&appName=forward") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "forward")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
