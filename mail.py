import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

now = datetime.now()

gmail = smtplib.SMTP("smtp.gmail.com", 587)
gmail.ehlo()
gmail.starttls()
gmail.ehlo()
gmail.login('< YOUR EMAIL HERE >', '< UNFORTUNATELY YOUR EMAIL PASSWORD HERE >')


sender_email = "< YOUR EMAIL HERE AGAIN >"
reciever_email = "< EMAIL TO WHICH YOU HAVE TO SEND STATUS UPDATE >"

with open ("intro.html", "r") as intro_html:
    introduction =intro_html.read()

with open ("work.html", "r") as work_html:
    workdone=work_html.read()

with open ("signature.html", "r") as myfile:
    signature=myfile.read()

msg = MIMEMultipart('alternative')
msg['Subject'] = "Status Update " + str(now.strftime("%d-%m-%Y"))
msg['From'] = sender_email
msg['To'] = reciever_email

html = introduction + "<br>" + workdone + "<br><br>" + signature

msg.attach(MIMEText(html, 'html'))

gmail.sendmail(sender_email, reciever_email, msg.as_string())
