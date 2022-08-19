import os
import time
import datetime
from colorama import *
from art import *
import smtplib  # Optional
from email.mime.text import *  # Optional 
from email.mime.multipart import * # Optional
from email.message import * #optional


#email function  (optional & advanced)
def gmail_send(subject, message, fromI, to, passI):
    global link
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromI, passI)
    msg            = EmailMessage()
    message        = f'{message}'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = fromI
    msg['To']      = to