

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]


print(len(known_users))

while True:
    print("Hi, my name is Travis")
    x = input("What is your name?: ").strip().capitalize()

    if x in known_users:
        print("Hello "+ x + " Your name has been recognised")
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            known_users.remove(x)
        elif remove == "n":
            print("You'll stay on the list")

    else:
        print("Hello "+ x + " Your name has not been recognised")
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(x)
        elif add_me == "n":
            print("You'll stay out of the list")
    
 

