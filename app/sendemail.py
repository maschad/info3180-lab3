import smtplib

def send(fromaddr,fromname,subject,msg):

    toaddr  = 'chad.nehemiah94@gmail.com'

    message = """From: {} <{}>

    To: {} Chad

    Subject: {}

    {}

    """

    messagetosend = message.format(
                                fromname,
                                fromaddr,
                                toaddr,
                                subject,
                                msg)

    # Credentials (if needed)

    username = 'chad.nehemiah94@gmail.com'

    password = 'eyjkezfhkjnyeqpn'


    # The actual mail send

    server = smtplib.SMTP('smtp.gmail.com:587')

    server.starttls()

    server.login(username,password)

    server.sendmail(fromaddr,toaddr, messagetosend)

    server.quit()