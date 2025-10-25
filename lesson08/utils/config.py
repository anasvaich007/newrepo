import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("YOUGILE_TOKEN")
BASE_URL = "https://ru.yougile.com/api-v2"
