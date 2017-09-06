from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = 587
username = "hellopycat@gmail.com"
password =  "katerina123"
from_email = username
to_list = ["kkampardi@gmail.com"]


try:
    # setup  the smtp connection
    conn = SMTP(host, port)
    conn.ehlo()
    conn.starttls()
    conn.login(username, password)

    # use standard way of calling an HTML message

    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Hello there"
    msg['From'] = from_email
    msg["To"] = to_list[0]


    plain_txt = "Testing the message"
    html_txt = """\
    <html>
        <head></head>
        <body>
            <p>Hey!<br/>
                Testing this email <b>message</b>. Made by <a href='http://kkabardi.me'>Pycat</a>.
            </p>
        </body>
    </html>
    """

    part_1 = MIMEText(plain_txt, 'plain')
    part_2 = MIMEText(html_txt, 'html')

    msg.attach(part_1)
    msg.attach(part_2)
    conn.sendmail(from_email, to_list, msg.as_string())
    conn.quit()
except SMTPException:
    print("error while sending the message")
