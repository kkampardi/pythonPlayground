
films = {
        "Finding Dory" : [3,5],
        "Bourne" : [18,5],
        "Tarzan": [15,2],
        "Ghost Busters": [12,5]
        }


while True:
    choice = input("What move do you want to watch?:").strip().title()
    print (choice)

    if choice in films:
        # check user age
        #  cast user input to int 
        age = int(input("How old are you?:").strip())
        if age >= films[choice][0]:
            # check enough seats
            numseats = films[choice][1]
            if numseats > 0:
                print ("enjoy the film")
                films[choice][1] = films[choice][1] -1
            else:
                print("Sorry there are no seats left")
        else:
            print("you are too yang to watch that film")
    else:
        print("We dont have that film")

        
