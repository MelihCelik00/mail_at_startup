#!/usr/bin/env python3
# Author: Melih Safa Çelik
# Date: September 13, 2021


import smtplib
from typing import Dict, Any
import ssl
from email.message import EmailMessage


receivers = ["yagizcanilbey1903@gmail.com", "melihsafa.c@gmail.com"]


def send_mail(mail_content: str) -> str:
    EMAIL_ADDRESS = "melihsafa.c@gmail.com"
    EMAIL_PASSWORD = "xxxxxxxxxxxxxxxx"
    msg = EmailMessage()
    msg["Subject"] = f"Sendmail SMTP Email test 001"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receivers 
    msg.set_content("This is a Sendmail test e-mail message 1")
    msg.add_alternative(mail_content, subtype="html")

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


send_mail("<h1>test_mail</h1>")
