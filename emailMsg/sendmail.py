import smtplib
import time

import json
import random
from email.message import EmailMessage 


EMAIL_ADDRESS = 'mallessamohamedamine@gmail.com'
EMAIL_PASSWORD = ''
contacts = ['osmbtrk@gmail.com', 'mallessamohamedamine@gmail.com'] 

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: 
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
    for contact in contacts:
        msg = EmailMessage()
        msg['Subject'] = 'Check out Bronx as a puppy!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = contact
        msg.set_content('This is a plain text email') 
        msg.add_alternative("""\<!DOCTYPE html><html> <body> <h1 style="color:SlateGray;">This is an HTML Email!</h1> </body></html>""", subtype='html') 
        smtp.send_message(msg)
        time.sleep(random.randrange(1, 4))
