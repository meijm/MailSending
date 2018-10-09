#Copyleft 2018, Mei Jiaming, Shanghaitech
#
from readmail import get_contacts, read_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

#socket.setdefaulttimeout(10)
MY_ADDRESS = 'si131_02_2018@163.com'
PASSWORD = 'Brother Young is the best TA!'

s= smtplib.SMTP(host='smtp.163.com', port=994)#change your prot !!!!!!
s.ehlo()
s.starttls()
s.login(MY_ADDRESS,PASSWORD)

names, emails = get_contacts('mycontacts.txt')
message_template = read_template('message.txt')

for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="This is TEST"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    
    del msg
s.quit()
