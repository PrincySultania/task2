import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("your_email-id","your_password")
message="""\
Subject: "Jenkins mlops task2 job's notification"

The code DID NOT run smoothly or produced invalid output.
"""
s.sendmail("your_email-id","receiver_email-id",message)
s.quit()
