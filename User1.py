#Ask user for name
name = input("What is your name?: ")
#ask for age
age = input("What is your age?: ")
#ask for city
city = input("In what city do you live in?: ") 
#ask what they enjoy
enjoy = input("What do you enjoy doing?: ")
# output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,enjoy)
#print output to screen
print(output)
