def send_mail(otp):
    import smtplib, ssl
    port = 995  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "lk9805320161@gmail.com" # Enter your address 
    receiver_email = "lk9805320161@gmail.com" # Enter receiver address
    password = "623028312"
    message = f"""\
	Subject: Hi there
	Your Otp is......>>{otp}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
import random as rm
otp=chr(rm.randint(65,90))+str(rm.randint(1,9))+chr(rm.randint(65,90))+str(rm.randint(1,9))+chr(rm.randint(65,90))+str(rm.randint(1,9))
print("Please check your Email for OTP")
send_mail(otp)
xx=input("Enter Otp...")
if xx==otp:
    print("Welcome toi my site.............")
else:
    print("Wrong OTP................")
