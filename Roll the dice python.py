# what the file name says...

import random
def rollDeDice():
    number = random.randint(1,6)
    print(number)
    runAgain()

def runAgain():
  roll = input("roll again?")
  if roll == "y":
    rollDeDice()
  elif roll == "n":
    print("ok")
  else:
    print("invalid input")
    runAgain()

rollDeDice()
