import smtplib

sender = 'meijm@outlook.com'
receivers = ['meijiaming0@163.com']

message = """ Hello meijm!
Cheers~
meijm 13262580357
"""

try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")

