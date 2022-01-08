import random

again = True

while again:
    print(random.randint(1, 100))
    another_roll = input("Want to roll the dice again? (y/n): ")
    if another_roll.lower() == "y":
        continue
    else:
        break