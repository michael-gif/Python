# just a little bit of hollywood action in a python file...

# This code was designed for the python editor online: https://python.codnex.net/
# All indents found in this code are two spaces.

import time
commence = str(input("activate?"))
if commence == "//y":
  activate = True
elif commence == "//n":
  activate = False
else:
  activate = "invalid"

class execution:
  def launch():
      array = ["- processing","- confirmed","- launching"]
      for j in range (0,3):
        print(array[j])
        time.sleep(1)
      time.sleep(2)
      print("- system hacked")
      print("- launch failure")

  def scan():
      print("- scanning")
      time.sleep(3)
      print("- scan complete")
      time.sleep(.5)
      print("- compiling visual data representation")
      time.sleep(5)
      
      # Put numbers into the layer variables below.
      # The layout of the variables below is exactly how it will be layed out when the code is executed.
      layer0 = [0,0,1,1]
      layer1 = [1,0,0,1]
      layer2 = [1,1,0,0]
      layer3 = [0,0,1,0]
      layer4 = [1,1,1,1]

      twoDarray = [layer0,layer1,layer2,layer3,layer4]

      layerSelection = 0

      for p in range(0,5):
        time.sleep(.25)
        print("".join(str(x) for x in twoDarray[layerSelection]))
        layerSelection += 1
        
      print("- visual data representation complete")
  
  def cancel():
      time.sleep(1)
      print("- cancelling")
      time.sleep(2)
      print("- cancelled")


def function (x):
  if x == True:
    command = input("-enter command")
    if command == "//launch":
      execution.launch()
    elif command == "//scan":
      execution.scan()     
    elif command == "//cancel":
      execution.cancel()
    else:
      print("- invalid command")
  elif x == False:
    print("- ended")
  elif x == "invalid":
    print("- invalid response")


function(activate)

