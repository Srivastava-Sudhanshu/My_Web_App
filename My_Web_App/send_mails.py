from datetime import datetime
import email
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os 
import logging
from tkinter.messagebox import OK
from turtle import done
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import codecs

from My_Web_App.settings import EMAIL_CREDENTIALS_PATH, EMAIL_PORT_NO, EMAIL_SERVER,EMAIL_TEMPLATE

def SendMailForDue(stud):
    try:
        logger = logging.getLogger('django')
        path = EMAIL_CREDENTIALS_PATH #For fetching the email and password from the file
        with open(path, 'r') as f:
            sender_email = f.readline()
            sender_email = sender_email[:-1]
            sender_password = f.readline()

        message = MIMEMultipart("alternative")
        message["Subject"] = "Fees Due!"
        message["From"] = sender_email
        message["To"] = stud.student.email

        # msg = EmailMessage()
        # msg['Subject'] = 'Fees Due!'
        # msg['From'] = sender_email
        # msg['To'] = stud.student.email
        # msg.set_content('Hello')
        html=""
        with codecs.open(EMAIL_TEMPLATE, 'r') as mail_template:
            html = mail_template.read()
        html = html.replace("$(name)",str(stud.student))
        html = html.replace("$(dueamount)",str(stud.due_amount))

        mail_template = MIMEText(html, "html")
        message.attach(mail_template)
        smtpobj = smtplib.SMTP(EMAIL_SERVER,EMAIL_PORT_NO)
        smtpobj.starttls()
        logger.info("Logging in to the sender's account" + str(datetime.now()))
        smtpobj.login(sender_email,sender_password)
        logger.info(f"Sending mail to {stud.student.email}:" + str(datetime.now()))
        
        response = smtpobj.send_message(message)
        if len(response):
            logger.info(f"Unable to send mail to {response}")
        else:
            logger.info(f"Mail sent to {stud.student.email}:" + str(datetime.now()))
    except Exception as e:
        logger.info(f"Error:{e}" + str(datetime.now()))
    finally:
        smtpobj.quit()
        return "Mail Sent"