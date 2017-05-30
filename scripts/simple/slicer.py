# get user email address

""" strip away all of the blank spaceces using the strip method """

email = input("What is your email address:").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") +1 :]
# format message

output = "Your user name is {} and your domain name is {}".format(user, domain)
# display output
print (output)
 

