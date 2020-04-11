# This code was designed for the python editor online: https://python.codnex.net/
# However any other Python editor may be used that uses two spaces as an indent.
# All indents found in this code are two spaces.
# WHEN INDENTING ANYTHING, MAKE SURE YOU DON'T USE THE TAB KEY. ALWAYS USE THE SPACE BAR

import time

# Put numbers into the layer variables below.
# The layout of the variables below is exactly how it will be layed out when the code is executed.
layer0 = [0,0,1,1]
layer1 = [1,0,0,1]
layer2 = [1,1,0,0]
layer3 = [0,0,1,0]
layer4 = [1,1,1,1]

twoDarray = [layer0,layer1,layer2,layer3,layer4]

layerSelection = 0

for x in range(0,5):
  time.sleep(.25)
  print("".join(str(x) for x in twoDarray[layerSelection]))
  layerSelection += 1
