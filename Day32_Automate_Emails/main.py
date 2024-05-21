"""Project: Automate Emails
Start: May 21st, 2024
Last touched: May 21st, 2024
Author: Madeleine L.
"""
# Simple Mail Transfer Protocol: Contains all the rules of how email is sent around the internet
# Skipping lesson for now as I don't want to create two new email addresses
import smtplib

EMAIL = "dummy1@provider.com"
PWD = "alesio39jdl"

with smtplib.SMTP("smtp.provider.com") as connection:
    connection.starttls()  # Encrypts email so it cannot be read if intercepted
    connection.login(user=EMAIL, password=PWD)
    connection.sendmail(from_addr=EMAIL, to_addrs="dummy2@provider.com", msg="Subject: Hello Dummy 2"
                                                                             "\n\n This is the body of my email")

