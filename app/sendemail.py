import smtplib

fromaddr = 'chad.nehemiah94@gmail.com'

toaddr  = '{{toaddr}}'

message = """From: {fromadd} <{fromname}>

To: {toaddr} <{toname}>

Subject: {subject}

{message}

"""

messagetosend = message.format(
                            fromname,
                            fromadd,
                            toname,
                            toaddr,
                            subject,
                            message)

# Credentials (if needed)

username = 'chad.nehemiah94@gmail.com'

password = '{eyjkezfhkjnyeqpn}'


# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr,toaddr, messagetosend)

server.quit()