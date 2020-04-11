# what the file name says...

import random
import time
maxCount = 1000
randomNum = random.randint(0,maxCount)
tries = 0
num = int(input("give me a number between 1 and 1000"))
while num != randomNum:
  randomNum = random.randint(0,maxCount)
  #print(randomNum)
  time.sleep(.01)
  tries += 1
print("Found #:" , num , ",\nTries:" , tries)
