import smtplib, ssl

sender = "example123@email.com"
recievers = "anotherexample123@email.com"

subject = 'Test Message'
message = """From: From Person
To: To Perso
Subject: SMTP e-mail test

This is a test e-mail message.
"""

ssl_context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl_context)
server.ehlo()
server.login("example123@email.com","atviwsxljjwgglws")#Revoked Code
result = server.sendmail(sender, recievers, message)
print("Send Message Successfull")