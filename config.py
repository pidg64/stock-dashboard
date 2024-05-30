import os

from dotenv import load_dotenv

load_dotenv()

alpha_vantage_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
