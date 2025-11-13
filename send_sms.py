# -*- coding: utf-8 -*-
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsms.settings')
django.setup()

from smsapp.sms_service import SparrowSMSService

def send_sms_backend():
    
    # Initialize SMS service
    sms_service = SparrowSMSService()
    
    # Your phone number and message
    phone_number = "9848044681"
    message = "Hello"
    
    print(f"To: {phone_number}")
    print(f"Message: {message}")
    print("\nSending...")
    
    # Send SMS directly
    result = sms_service.send_sms(phone_number, message)
    
    print("\n" + "=" * 50)
    if result['success']:
        print("SUCCESS! SMS sent!")
        print(f"Message ID: {result.get('message_id')}")
        print("\nCheck your phone for the message!")
    else:
        print(f"FAILED: {result.get('error')}")
        print("\nCheck your .env file and Sparrow SMS token")
    print("=" * 50)

if __name__ == "__main__":
    send_sms_backend()
