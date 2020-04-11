# what the name of the file says...

import random
letterOptions = ["b","c","d","f","h"]
name = ["adam","andrew","anthony","alex","alexa","arthur"]
swapLetter = ["e","i"]

nameToMod = list(random.choice(name))
i = 0
for x in range(len(nameToMod)):
  if nameToMod[i] == "a" or nameToMod[i] == "t":
    nameToMod[i] = random.choice(swapLetter)
  if nameToMod[i] == "h":
    nameToMod[i] = "u"
    i += 1
  else:
    i += 1
    
print("".join(nameToMod))
