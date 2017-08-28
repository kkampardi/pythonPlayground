import datetime


class MessageUser():
	user_details = []
	messages = []
	base_message = """ Hi {name}
				Thank you for the purchase on {date}
				We hope you are exited about using it. Just
				a reminder the purchase total was ${total}.

				Team CFE
				"""

	def add_user(self, name, amount, email=None):
		# check if name is capitalized
		name = name[0].upper() + name[1:].lower()
		detail = {
			"name": name,
			"amount": amount,
		}

		today = datetime.date.today()
		date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
		detail['date'] = date_text

		if email is not None:
			detail["email"] = email

		self.user_details.append(detail)

	def get_details(self):
		return self.user_details


	def make_messages(self):
		if len(self.user_details) > 0:
			for detail in self.get_details():
				name = detail["name"]
				amount = "%.2f" %(detail["ammount"])
				date = detail[date]
				message = self.base_message
				new_msg = unf_message.format(
					name=name,
					date=text,
					total=new_amount
					)
				self.messages.append(new_msg)

		return []
					

obj = MessageUser()
obj.add_user("Justin", 123.32, email='hello@kabardi.me')
obj.add_user("Kate", 332.33)
obj.add_user("Ore", 43.00)

print (obj.get_details())
