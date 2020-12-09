students = {
    "male" : ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Ellie"]
    }

for key in students.keys():
    print(key)


for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)



