import smtplib

def send(fromaddr,fromname,toname,subject,msg):

    toaddr  = 'chad.nehemiah94@gmail.com'

    message = """From: {fromaddr} <{fromname}>

    To: {toaddr} <{toname}>

    Subject: {subject}

    {msg}

    """

    messagetosend = message.format(
                                fromname,
                                fromaddr,
                                toname,
                                toaddr,
                                subject,
                                message)

    # Credentials (if needed)

    username = 'chad.nehemiah94@gmail.com'

    password = 'eyjkezfhkjnyeqpn'


    # The actual mail send

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()

    server.login(username,password)

    server.sendmail(fromaddr,toaddr, messagetosend)

    server.quit()