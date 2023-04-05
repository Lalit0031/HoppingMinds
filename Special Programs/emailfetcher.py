import mailbox
import csv 
import email
import imaplib
import getpass, poplib


username=input("Enter your emailId : ")
password=input("Enter Your Password : ")
c = imaplib.IMAP4_SSL("imap.gmail.com")
try:
    c.login(username,password)

    c.select("inbox")

    n=int(input('Enter the number of emails you want to analyse : '))#no. of emails to b analysed

    print("Please wait for sometime!.\nWe r fetching data.")

    with open (username[:5]+"Emails"+".csv",'w',newline='') as o:
        writer=csv.writer(o)
        writer.writerow([ 'subject', 'to', 'from' ,'Date'])
        for i in range(1,n):
            typ, msg_data = c.fetch(str(i), '(RFC822)')
            for response_part in msg_data:	
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                # for header in [ 'subject', 'to', 'from' ,'Date']:
                    # print ('%-8s: %s' % (header.upper(), msg[header]))
                    # print (msg[header])
                    
                    writer.writerow([msg['subject'],msg['to'],msg['from'],msg['Date']])
        print("File Writen Succesfully")
except Exception as msg:
    print('Wrong UserName or Password!',msg)
#https://myaccount.google.com/