import random

print('______________________________________')
print('       Hello - Guess the number')
print('______________________________________')
print('')

# while guess != the_number:
#     guess = int(input('Guess a number between 0 and 100: '))
#
#     if guess > the_number:
#         print('{} is to hight'.format(guess))
#     elif guess < the_number:
#         print('{} is to low'.format(guess))
#     else:
#         print('You win')

# recursive approach
def guess_num(the_number, guess):
    guess = int(input('Guess a number between 0 and 100: '))
    if guess != the_number:
        if guess > the_number:
            print('{} is to hight'.format(guess))
            guess_num(the_number, guess)
        elif guess < the_number:
            print('{} is to low'.format(guess))
            guess_num(the_number, guess)
    else:
        print('You win')

if __name__ == '__main__':
    the_number = random.randint(0, 100)
    guess = -1
    guess_num(the_number, guess)