import os
from dotenv import load_dotenv

load_dotenv()

class SparrowSMSConfig:
    API_KEY = os.getenv('SPARROW_SMS_API_KEY')
    FROM = os.getenv('SPARROW_SMS_FROM', 'TestSMS')
    BASE_URL = 'https://api.sparrowsms.com/v2/'
    
    @classmethod
    def validate_config(cls):
        if not cls.API_KEY:
            raise ValueError("❌ SPARROW_SMS_API_KEY is missing from .env file")
        if not cls.FROM:
            raise ValueError("❌ SPARROW_SMS_FROM is missing from .env file")
        print("✅ SMS configuration is valid")