import random as rd
easy = 1
medium = 2
hard = 3
difficulty = medium

player_health = 50

potion_health = int(rd.randint(25,50) / difficulty)

new_health = player_health + potion_health

print(new_health) 
