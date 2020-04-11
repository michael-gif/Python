# this is a test based adventure game in python

key = False
gun = False
zombiesKilled = False

def bottomLeft():
    global gun
    global key
    print("")
    print("You enter a room full of guns.")
    print("You look through the door in front of you and see a room full of zombies")
    print("The door in front of you is locked")

    dot = True
    while dot == True:
        response = input("Your options are east, north")
        if response == "east":
            bottomMiddle()
        elif response == "north":
          if key == True:
              if gun == True:
                  middleLeft()
              else:
                  print("Don't you want to prepare yourself first?")
          else:
              print("The door is locked")
        elif response == "take a gun":
            if gun == False:
                gun = True
                print("")
                print("You take a gun")
            else:
                print("You already have a gun")
        else:
          print("")
          print("Can't do that")


def bottomMiddle():
    print("")
    print("You are in a room that is dark. There is silence")
    print("All you know is that you are in a 3 by 3 grid of rooms.")
    print("You have to get the the top right room")
    print("You always face the top of grid.")
    print("But using your peripheral vision you can see if there is a door next to you.")
    dot = True
    while dot == True:
      response = input("Your options are west, north")
      if response == "west":
          bottomLeft()
      elif response == "north":
          middleMiddle()
      else:
          print("")
          print("Can't do that")


def bottomRight():
    global key
    print("")
    print("You enter a room with a metal table in the center")
    print("On the table is a key")
    dot = True
    while dot == True:
        response = input("Your option is north")
        if response == "north":
            middleRight()
        elif response == "take the key":
          if key == False:
              print("")
              print("You take the key")
              key = True
          else:
              print("")
              print("You already have the key")
        else:
            print("")
            print("Can't do that")


def middleMiddle():
    global key
    global gun
    print("")
    print("You enter an empty room with cracks all over the walls.")
    print("There is a door to you left and a door to your right.")
    dot = True
    while dot == True:
        response = input("Your options are west, east, south")
        if response == "west":
            if key == True:
                if gun == True:
                    middleLeft()
                else:
                    print("")
                    print("Don't you want to prepare yourself first?")
            else:
                print("")
                print("You look through the door in front of you and see a room full of zombies")
                print("The door is locked")
        elif response == "east":
            middleRight()
        elif response == "south":
            bottomMiddle()
        else:
            print("")
            print("Can't do that")


def middleRight():
    print("")
    print("You enter a room which appears to be an office.")
    print("There is no computer, everything has been destroyed.")
    print("The place appears to have been ransacked")
    dot = True
    while dot == True:
        response = input("Your option is west, south")
        if response == "west":
            middleMiddle()
        elif response == "south":
            bottomRight()
        else:
            print("")
            print("Can't do that")


def middleLeft():
    global zombiesKilled
    if zombiesKilled == False:
        print("")
        print("You enter a room full of flesh hungry zombies.")
        print("The light in the ceiling suddenly turns off and there is darkness.")
        print("You react immediately to the zombies")
        print("Thanks to your quick moves, you turn the zombies into swiss cheese with your gun.")
        print("All around you are dead zombies.")
        zombiesKilled = True
    else:
        print("")
        print("You are back in the room which had the zombies in")
        print("All around you are dead zombies.")
    dot = True
    while dot == True:
        response = input("Your options are north, east, south")
        if response == "north":
            topLeft()
        elif response == "east":
            middleMiddle()
        elif response == "south":
            bottomLeft()
        else:
            print("")
            print("Can't do that")


def topLeft():
    print("")
    print("You enter a room full of skulls.")
    print("There is blood everywhere. It appears to have been a massacre")
    print("You side step throught all the flesh, brains and blood to a door.")
    dot = True
    while dot == True:
        response = input("Your options are east, south")
        if response == "east":
            topMiddle()
        elif response == "south":
            middleLeft()
        else:
            print("")
            print("Can't do that")

def topMiddle():
    print("")
    print("You step through the rustic looking door and see a dead body in front of you.")
    print("You roll it over to reveal it's face.")
    print("It turns out to be the person who put you in this grid.")
    print("He has a massive hole going straight thorugh his head.")
    print("It's so big that you can see his brains. Or what is left of them...")
    print("A white door is to the east of you. A blood splatter on it.")
    dot = True
    while dot == True:
        response = input("")
        if response == "east":
            topRight()
        elif response == "west":
            topLeft()
        else:
            print("")
            print("Can't do that")


def topRight():
    print("")
    print("You step through the white door. There is a chair in front of you.")
    print("The chair has it's back to you. Someone is sitting in it.")
    print("They swivel round to face you. There is a gun in there hand...")
    print("Before you have time to say anything, the trigger is pulled.")
    print("You feel a prick in your head, then nothing. Everything goes white.")
    print("It's over.")


bottomMiddle()
