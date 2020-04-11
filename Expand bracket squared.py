# does what it says in the title

quadratic = input("enter quadratic in the following format: (x+y)^z")
a = int(quadratic[1])
b = int(quadratic[3])
def expansion():
  global a, b
  coeifficientSquare = a * a
  coeifficientX = a * b
  coeifficientX = coeifficientX * 2
  term = b * b
  print(coeifficientSquare , "x^2 + " , coeifficientX , "x + " , term)

expansion()
