import random
again = True

while again:
  print(random.randint(1, 6))
  new_roll = str(input("Do you want to roll the dice again? (y/n) "))
  if new_roll.lower() == "y":
    continue
  else:
    break
