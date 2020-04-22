import pandas as pd
import numpy as np
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

MY_ADDRESS='meijm@outlook.com'
PASSWORD='xxxxxxxx'

data=pd.read_excel('total.xlsx')
length=data.shape[0]
message_template=Template('Hello $name, your homework one has a total score of $Total, including $Q1 for the first question, $Q2 for the second question, and $Q3 for the third question. If you have any questions about the score, please contact the TA before April 24.')
#message_template=Template('$name $email $Q1 $Q2 $Q3 $Total')


s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.ehlo()
s.starttls()
s.login(MY_ADDRESS,PASSWORD)

for i in range(length):
    data_i=dict(data.loc[i])
    msg = MIMEMultipart()       # create a message
    message = message_template.substitute(data_i)
    print(data_i)

    msg['From']=MY_ADDRESS
    msg['To']=data_i['email']
    msg['Subject']="Homework1 score"
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    print("SENT EMAIL TO ", data_i['name'])
    del msg
    #add waiting time
    print('type anything or nothing and press Enter (Prevent sending blocking ):')
    x = input()
    print('Hello, ' + x)
s.quit()

