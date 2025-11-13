import re

class SMSUtils:
    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        """
        Validate Nepali phone number format (98XXXXXXXX)
        """
        if not phone_number:
            return False
            
        cleaned = re.sub(r'[\s\-+]', '', phone_number)
        pattern = r'^98[1-9]\d{7}$'
        
        is_valid = bool(re.match(pattern, cleaned))
        if not is_valid:
            print(f"❌ Invalid phone number: {phone_number}")
        else:
            print(f"✅ Valid phone number: {cleaned}")
            
        return is_valid
    
    @staticmethod
    def format_phone_number(phone_number: str) -> str:
        """
        Format phone number to 98XXXXXXXX format
        """
        if not phone_number:
            return ""
            
        cleaned = re.sub(r'[\s\-+]', '', phone_number)
        
        # Remove country code if present
        if cleaned.startswith('977'):
            cleaned = cleaned[3:]
            
        # Remove leading zero if present
        if cleaned.startswith('0'):
            cleaned = cleaned[1:]
            
        return cleaned