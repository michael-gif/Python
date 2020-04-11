# crap attempt at machine learning
# there isn't a neural network in this so it isn't even machine learning
primes = []
notPrimes = []
def trainer(): 
  values = list(raw_input("enter some values"))
  a = 0
  for x in range (len(values)):
    if values[a] in primes:
        a += 1
    else:
      if values[a] not in notPrimes:
        response = raw_input(values[a] + " is a prime number. yes or no?")
        if response == "y":
          if values[a] in primes:
            a += 1
          else:
            primes.append(values[a])
            a +=1
        elif response == "n":
          notPrimes.append(values[a])
          a += 1
      else:
        a += 1
  comparator()

def comparator():
  newValues = list(raw_input("enter some more values"))
  b = 0
  newPrimes = []
  for y in range (len(newValues)):
    if newValues[b] in primes:
      if newValues[b] in newPrimes:
        b += 1
      else:
        newPrimes.append(newValues[b])
        b += 1
    else:
      b += 1

  print("These were the numbers you entered: " , newValues)
  print("These are the prime numbers I found: " , newPrimes)
  response = raw_input("Did i miss any primes?")
  if response == "y":
    newResponse = list(raw_input("enter the ones i missed"))
    if newResponse in primes:
        print(primes)
        comparator()
    else:
        bg = 0
        for d in range (0,len(newResponse)):
            primes.append(newResponse[bg])
            bg += 1
        print(primes)
  comparator()


trainer()
