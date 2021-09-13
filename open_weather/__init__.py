import os
from dotenv import load_dotenv

# Import open weather api key from .env file
load_dotenv()

OPENW_API_KEY = os.getenv("OPENW_API_KEY")