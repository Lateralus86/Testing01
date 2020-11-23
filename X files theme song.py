#ask username
#Show username and welcome user
username = input("What is your username?: ").strip()
print("Hello " + username + " Can you please tell me your age and where do you live?")


#Ask for age and city
age = input("What is your age?: ").strip()

city = input("Where do you live (city): ").strip()

#Format message

output = "You live in {} and your age is {}".format(city,age)

#display output
print(output)

