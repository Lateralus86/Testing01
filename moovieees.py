#Cinema
####add films
films = {
    "Top Gun":[3,4],
    "Blade Runner":[18,5],
    "Eyes Wide Shut":[12,5]
    }




####input what film
while True:
    choice = input("What film would you like to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())

        
        if age >= films[choice][0]:
            
            if films[choice][1]>0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, sold out")
        else:
            print("You're too young!")
    else:
        print("Movie not available")

