#!/usr/bin/env python3
# Author: Melih Safa Çelik
# Date: September 13, 2021


import smtplib

sender = 'melihsafa.c@gmail.com'
receivers = ['melihsafa.c@gmail.com']

message = '''From: No Reply <melihsafa.c@gmail.com>
To: Melih Safa Celik <melihsafa.c@gmail.com>
Subject: Sendmail SMTP Email test 001

This is a Sendmail test e-mail message 1.
'''

"""
For gmail use smtp.gmail.com
For outlook/hotmail use smtp-mail.outlook.com with the port number 587
"""
try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sender, receivers, message)
	print('Successfully sent email')
except SMTPException:
	print('Error: unable to send email')


