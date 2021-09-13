#!/usr/bin/env python3
# Author: Melih Safa Çelik
# Date: September 13, 2021


import smtplib
from typing import Dict, Any
from email.message import EmailMessage



def send_mail(mail_content: str) -> str:
    EMAIL_ADDRESS = "melihsafa.c@gmail.com"
    EMAIL_PASSWORD = "password"
    msg = EmailMessage()
    msg["Subject"] = f"Sendmail SMTP Email test 001"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receivers 
    msg.set_content("This is a Sendmail test e-mail message 1")
    msg.add_alternative(mail_content, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


send_mail("<h1>test_mail</h1>")
