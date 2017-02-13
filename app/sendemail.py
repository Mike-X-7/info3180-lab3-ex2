import smtplib


            
def send_email(from_name,from_email,subject,msg):
    toname = "Michael Green"
    toaddr = 'likemike303@gmail.com'
    message = """From: {} <{}>
    To: {} <{}>
    Subject: {}
    {}
    """
    
    
   
 
    messagetosend = message.format(
                                 from_name,
                                 from_email,
                                  toname,
                                 toaddr,
                                 subject,
                                 msg)

    # Credentials (if needed)
    # Username and password removed for privacy purposes.
    username = ''
    password = ''

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, toaddr, messagetosend)
    server.quit()