#email adress
email = input("What is your email?: ").strip()

#slice username
username = email[:email.index("@")]

#slice domain
domain_name = email[email.index("@")+1:]

#format message
output = "Your username is {} and your domain name is {}".format(username,domain_name)


#output display
print(output)

