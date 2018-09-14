films = {
    "Finding Dorty":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    
    choice=input("What movie would you like to see?: ").strip().title()
    
    if choice in films:
        #check enough seats            
        if films[choice][1] > 0:        
            #check user age
            age = int(input("How old are you?").strip())
            if age >= films[choice][0]:
                films[choice][1]=films[choice][1]-1
                print("Thanks! Enjoy the show!")
            else:
                print("Sorry, but you aren't old enough to see the movie.")
        else:
            print("Sorry, but that movie is sold out!")
    else:
        print("Sorry! We aren't showing that film.")
