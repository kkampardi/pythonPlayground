from smtplib import SMTP, SMTPAuthenticationError, SMTPException


host = "smtp.gmail.com"
port = 587
username = "hellopycat@gmail.com"
password =  "katerina123"
from_email = username
to_list = ["otsakir@gmail.com"]
# setup  the smtp connection
conn = SMTP(host, port)
conn.ehlo()
conn.starttls()

# handle wrong credentials exceptions
try:
    conn.login(username, password)
    conn.sendmail(from_email, to_list, "Hi Orestis")
except SMTPAuthenticationError:
    print ("Could not login")
except:
    print("an error occured")
conn.quit()