


""" as user for name """
name = input("What is your name: ")
""" ask user for age """
age = input("How old are you: ")
""" ask user for city """
city = input("Where do you live")
""" ask user what they enjoy """
love = input("What do you love: ")
""" print output to the screen """
output_string  = "Your name is {} and you are {} years old.You live in {} and tou love {}"
output  = output_string.format(name, age, city, love)

print (output)
