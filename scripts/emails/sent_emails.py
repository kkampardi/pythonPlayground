import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "hellopycat@gmail.com"
password =  "katerina123"
from_email = username
to_list = ["kkampardi@gmail.com"]



class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}!

Thank you for the purchase on {date}.
In publishing and graphic design, lorem ipsum
is a filler text commonly used to demonstrate
the graphic elements of a document or visual
presentation. Replacing meaningful content with
placeholder text allows designers to design the
form of the content before the content itself has
been produced.Just as a reminder the purcase total was ${total}.

Cheers

Pycat

"""

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower() 
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        } 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []

    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username, password)
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Billing Update!"
                    the_msg["From"] = from_email
                    the_msg["To"]  = user_email
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("There was an error while sending this message !")
            return True
        return False


obj = MessageUser()
obj.add_user("Katerina", 123.32, email='kabardi.cat@gmail.com')
obj.add_user("Pycat", 94.23, email='kkampardi@gmail.com')
obj.add_user("Orestis", 94.23, email='otskir@gmail.com')

obj.get_details()

obj.send_email()
