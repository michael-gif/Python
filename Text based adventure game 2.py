# it's a text based adventure game
'''
cr = corridor

you can figure out the pattern here:

ml = middle left
br = bottom right
mr = middle right

'''

crPos = 1
inventory = []
crPosBits = ["You start in a long corridor.", "You are back in the long corridor.", "You take the sunglasses and put them on.", "You take out the sunglasses again and put them on."]
actionResults = [" There are three doors on the left side and three on the right. You are facing the end of the corridor. You are facing North. You will always face North. You can go North, East, West", " A message displays in the lenses and a speaker starts playing it into your ear. It says: 'Greetings young one, you have been put into this puzzle to be tested on your brain function. Remember, this is for the greater good, and people will benefit from this. Menagol forever.' You take of the sunglasses and put them in your pocket."]
crLights = False
sunglasses = False
brKey = False
weapon = False
trap = 0
mlTorch= False
myles = False

def crDes(crPos):
  global crLights
  if crPos == 0:
    print(crPosBits[0] + actionResults[0])    
  elif crPos == 1:
    print(crPosBits[1] + actionResults[0])
  elif crPos == 2:
    print("You are in the middle of the corridor. There is a door to the left of you to the right of you. You can go North, East, South, West") 
  else:
    print("You are at the end of the corridor. There is a door to the left of you, to the right of you and in front of you. You can go North, East, South, West")

def cr():
  global crPos, action
  action = input("")
  if action == "north":
    if crLights == True:
      if crPos < 3:
        crPos += 1
        crDes(crPos)
        cr()
      else:
        print("Can't do that")
        cr()
    else:
      print("You can't see what you are doing. It is too dark.")
      cr()
  elif action == "west":
      if crPos == 1:
        bl(0)
      elif crPos == 2:
        if crLights == True:
          ml()
        else:
          print("You can't see what you are doing. It is too dark.")
          cr()
  elif action == "south":
    if crLights == True:
      if crPos > 1:  
        crPos -= 1
        crDes(crPos)
        cr()
      else:
        print("Can't do that")
        cr()
    else:
      print("You can't see what you are doing. It is too dark.")
      cr()
  elif action == "east":
    if crLights == True:
      if crPos == 1:  
        br(0)
      elif crPos == 2:
        mr()
    else:
      print("You can't see what you are doing. It is too dark.")
      cr()
  elif action == "inventory":
    print("\n".join(inventory))
    cr()
  else:
    print("Can't do that")
    cr()

def bl(act):
  global action, crLights, sunglasses
  if act == 0:
    if crLights == False:
      print("You enter a room with cracked cobblestone walls, and scratches all over the floor. There is minimal light in the room except for the corner. There is a light shining down on a chain that is hanging from the ceiling.")
      bl(1)
    else:
      print("You re-enter the room with the cracked cobblestone walls and the scratches all over the floor.")
      bl(1)
  else:
    action = input("")
    if action == "pull chain":
      print("You pull the chain and suddenly there is light in the corridor and in the room you are in. You see some sunglasses in the other corner of the room.")
      crLights = True
      bl(1)
    elif action == "take sunglasses":
      if crLights == True:
        print(crPosBits[2] + actionResults[1])
        inventory.append("Sunglasses")
        sunglasses = True
        bl(1)
      else:
        print("I can't see any sunglasses, it's so dark in here!")
        bl(1)
    elif action == "put on sunglasses":
      if sunglasses == True:
        print(crPosBits[3] + actionResults[1])
        bl(1)
      else:
        print("I don't have any sunglasses.")
        bl(1)
    elif action == "east":
      crDes(crPos)
      cr()
    elif action == "inventory":
      print("\n".join(inventory))
      bl(1)
    else:
      print("Can't do that")
      bl(1)

def br(act2):
  global brKey, weapon
  if act2 == 0:
    if brKey == False:
      print("The door to this room is locked. I'll have to find the key")
      br(1)
    else:
      if weapon == False:
        print("You enter the room and find a whole variety of weapons. All of them have been designed to do the same thing: kill the undead. I might want to *take a weapon*. there is a door to the north")
        br(1)
      else:
        print("You re-enter the room full of weapons.")
        br(1)
  else:
    action = input("")
    if action == "take a weapon":
      if weapon == False:
          print("You take one of the blood thirsty weapons")
          weapon = True
          inventory.append("A weapon")
          br(1)
      else:
        print("You already have one weapon, that is probably enough")
        br(1)
    elif action == "west":
      crDes(crPos)
      cr()
    elif action == "inventory":
      print("\n".join(inventory))
      br(1)
    elif action == "put on sunglasses":
      if sunglasses == True:
        print(crPosBits[3] + actionResults[1])
        br(1)
      else:
        print("I don't have any sunglasses.")
    else:
      print("Can't do that")
      br(1)

def ml():
  global trap, mlTorch
  if mlTorch == False:
    trap = 0
  else:
    trap = 1
  if trap == 0:
    print("You enter a room full of nothing. Not even air. There is an empty torch holder on the wall. A trap launches you into a pit below and the whole place turns into a vacuum. You explode.")
  elif trap == 1:
    print("You enter the room and put the torch into the torch holder, but you find that there is nothing in the room. But suddenly, a panel in the flush ceiling slides open slowly, and a man falls out of the ceiling. He stands up and says:'Hi! My name is Myles and I will follow you for the rest of the time you are here.'")
    trap += 1
    myles == True
    mlTorch = False
    inventory.append("Myles")
  else:
    print("You re-enter the room full of nothing. There is nothing there.")
  action = input("")
  if action == "east":
    crDes(2)
    cr()
  elif action == "kill myles":
    if weapon == True:
      print("You pull out your weapon, and kill myles. But suddenly, Myles stands up again and says to you 'What is your mission?'. You reply 'To get out of this place.'. He says 'You killed me, therefore you have failed that mission.'. He takes your weapon, and kills you in cold blood.")
  elif action == "put on sunglasses":
    if sunglasses == True:
      print(crPosBits[3] + actionResults[1])
      ml()
    else:
      print("I don't have any sunglasses.")
  else:
    print("Can't do that")

def mr():
  global mlTorch, myles
  if myles == False:
    if mlTorch == False:
      print("When you enter the room it is completely dark. there is no light anywhere, the light shining in from the corridor doesn't do anything. You slowly walk into the room further and further, while on high alert. Then you stumble on something. It is a battery powered flame torch.")
  else:
    print("You walk back into the room of darkness, however it isn't dark anymore. You look at Myles and see that he is glowing! He pulses every now and then. You continue turning your head and see that there is a key behind a glass window. You cannot break the glass.")
  action = input("")
  if action == "take torch":
    if mlTorch == False:
      print("You take the torch")
      mlTorch = True
      inventory.append("Flame torch")
      mr()
    else:
      print("You already have the torch")
  elif action == "west":
    crDes(2)
    cr()
  elif action == "put on sunglasses":
    if sunglasses == True:
      print(crPosBits[3] + actionResults[1])
      mr()
    else:
      print("I don't have any sunglasses.")
  else:
    print("Can't do that.")
    mr()

crDes(0)
cr()
