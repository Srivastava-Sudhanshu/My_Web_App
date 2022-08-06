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

from My_Web_App.settings import EMAIL_CREDENTIALS_PATH, EMAIL_PORT_NO, EMAIL_SERVER

def SendMail(stud):
    logger = logging.getLogger('django')
    try:
        flag = False
        path = EMAIL_CREDENTIALS_PATH
        with open(path, 'r') as f:
            sender_email = f.readline()
            sender_email = sender_email[:-1]
            sender_password = f.readline()
        message = MIMEMultipart("alternative")
        message["Subject"] = stud.mailsubject
        message["From"] = sender_email
        message["To"] = stud.email
        html = ""
        with codecs.open(stud.emailTemplate, 'r') as mail_template:
            html = mail_template.read()
        html = html.replace("$(name)", str(stud.name))
        html = html.replace("$(purposeobject)", str(stud.purposeobject))
        mail_template = MIMEText(html, "html")
        message.attach(mail_template)
        smtpobj = smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT_NO)
        smtpobj.starttls()
        logger.info("Logging in to the sender's account" + str(datetime.now()))
        smtpobj.login(sender_email, sender_password)
        logger.info(f"Sending mail to {stud.email}:{str(datetime.now())}")
        response = smtpobj.send_message(message)
        if len(response):
            logger.info(f"Unable to send mail to {response}")
        else:
            logger.info(f"Mail sent to {stud.email}:{str(datetime.now())}")
            flag = True
    except Exception as e:
        logger.info(f"Error:{e}{str(datetime.now())}")
    finally:
        smtpobj.quit()
        return flag
        
                