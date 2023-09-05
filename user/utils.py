from django.core.mail import EmailMessage
from rest_framework.response import Response
import random

#method to send mail.
class Utils:
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to = [data['to_email']])
        email.send()
        return Response('Email sent successfully!')
    
#method to generate OTP
def otpgenerator():
    rand_no = [x for x in range(10)]
    code_items_for_otp = []

    for i in range(6):
        num = random.choice(rand_no)
        code_items_for_otp.append(num)
        code_string = "".join(str(item) for item in code_items_for_otp)

    return code_string

#method to validate OTP
def checkOTP(otp, saved_otp_instance):
    if saved_otp_instance.otp == otp:
        return True
    else:
        return False
        

#method to delete OTP
def deleteOTP(saved_otp_instance):
    saved_otp_instance.delete()
    
