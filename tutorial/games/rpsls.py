# Rock-paper-scissors-lizard-Spock template

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print ("Invalide name!")
    # don't forget to return the result!
    return number


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print ("Invalid choice of number")

    # convert number to a name using if/elif/else
    # don't forget to return the result!
    return name

def rpsls(player_choice):
    # delete the following pass statement and fill in your code below

    # print a blank line to separate consecutive games
    print ('\n')

    # print out the message for the player's choice
    print ("You chose: " + player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    print ("\n")

    # compute random guess for comp_number using random.randrange()
    # convert comp_number to comp_choice using the function number_to_name()
    # print out the message for computer's choice
    comp_num = random.randrange(0,4)
    player_num = name_to_number(player_choice)

    comp_choice = number_to_name(comp_num)

    print ("Computer choses: " + comp_choice)

    # compute difference of comp_number and player_number modulo five
    print(comp_num, player_num)

    diff = comp_num - player_num %5

    # use if/elif/else to determine winner, print winner message
    if diff > 0:
        print ("Computer Wins!!")
    elif diff < 0:
        print ("Player Wins!!")
    else:
        print ("Raw!")

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
