import smtplib

def send(fromadd,fromname,toname,subject,msg):

    toaddr  = 'chad.nehemiah94@gmail.com'

    message = """From: {fromadd} <{fromname}>

    To: {toaddr} <{toname}>

    Subject: {subject}

    {msg}

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

    server.sendmail(fromadd,toaddr, messagetosend)

    server.quit()