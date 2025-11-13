import os
import django
from dotenv import load_dotenv

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsms.settings')
django.setup()

from smsapp.sms_service import SparrowSMSService
from smsapp.utils import SMSUtils

def main():
    print("=" * 50)
    print("🚀 TESTING SPARROW SMS INTEGRATION")
    print("=" * 50)
    
    # Initialize services
    sms_service = SparrowSMSService()
    utils = SMSUtils()
    
    # Your actual phone number
    test_phone = "9848044681"
    
    print(f"\n1. 📱 Testing with phone: {test_phone}")
    
    # Validate phone number
    formatted_phone = utils.format_phone_number(test_phone)
    if not utils.validate_phone_number(formatted_phone):
        print("❌ Please use a valid Nepali phone number (98XXXXXXXX)")
        return
    
    print("✅ Phone number valid")
    
    # SKIP BALANCE CHECK and go straight to SMS sending
    print("\n2. ⚡ Skipping balance check (proceeding to send SMS)...")
    print("   Note: Balance check may fail due to API permissions")
    
    print("\n3. 📤 Sending test SMS...")
    test_message = "Hello! This is a test message from your Django app. 🎉"
    print(f"   Message: '{test_message}'")
    
    result = sms_service.send_sms(formatted_phone, test_message)
    
    print("\n" + "=" * 50)
    if result['success']:
        print("🎉 SUCCESS! SMS integration is working perfectly!")
        print(f"📨 Message ID: {result.get('message_id')}")
        print("\n📱 Please check your phone 9848044681 for the message!")
        print("⏰ It should arrive within 30 seconds.")
    else:
        print(f"❌ FAILED: {result.get('error')}")
        print("\n🔧 Troubleshooting tips:")
        
        error_msg = result.get('error', '').lower()
        if 'balance' in error_msg or 'credit' in error_msg:
            print("   - Low balance: Add funds to Sparrow SMS account")
        elif 'sender' in error_msg:
            print("   - Sender ID issue: Try different Sender ID in .env")
            print("     Try: Demo, Info, Alert, Notify, or TestSMS")
        elif 'token' in error_msg or 'auth' in error_msg:
            print("   - Invalid API token: Check your .env file")
        elif 'number' in error_msg:
            print("   - Phone number issue: Verify 9848044681 is correct")
        else:
            print("   - Check Sparrow SMS dashboard for detailed errors")
    print("=" * 50)

if __name__ == "__main__":
    main()