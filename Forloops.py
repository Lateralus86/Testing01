###De a 1 lento###
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

###de a 1 rapido##3
for num in range(1,11):
    print(num)

#### de a 2
for num in range(1,11,2):
    print(num)

####vocales en hello
vowels = 0
conson = 0
for letter in "hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        conson = conson + 1


print("There are {} vowels").format(vowels)
print("There are {} consonants").format(conson)


