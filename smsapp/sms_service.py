import requests
import logging
from smsapp.sms_config import SparrowSMSConfig

# Setup logging
logger = logging.getLogger(__name__)

class SparrowSMSService:
    def __init__(self):
        SparrowSMSConfig.validate_config()
        self.api_key = SparrowSMSConfig.API_KEY
        self.from_name = SparrowSMSConfig.FROM
        self.base_url = SparrowSMSConfig.BASE_URL
        
    def send_sms(self, to: str, message: str) -> dict:
        """
        Send SMS to a single phone number
        """
        endpoint = f"{self.base_url}sms/"
        
        payload = {
            'token': self.api_key,
            'from': self.from_name,
            'to': to,
            'text': message
        }
        
        try:
            print(f"📤 Sending SMS to {to}...")
            response = requests.post(endpoint, data=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            print(f"✅ SMS sent successfully! Message ID: {result.get('id')}")
            
            return {
                'success': True,
                'message_id': result.get('id'),
                'response': result
            }
            
        except requests.exceptions.RequestException as e:
            error_msg = f"❌ Failed to send SMS: {str(e)}"
            print(error_msg)
            return {
                'success': False,
                'error': str(e)
            }
    
    def check_balance(self) -> float:
        """
        Check available SMS balance
        """
        endpoint = f"{self.base_url}credit/"
        params = {'token': self.api_key}
        
        try:
            print("💰 Checking balance...")
            response = requests.get(endpoint, params=params, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            balance = float(result.get('credit', 0))
            print(f"✅ Available balance: {balance}")
            
            return balance
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to check balance: {str(e)}")
            return 0