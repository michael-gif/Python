#set a fake date and time

import datetime
def setReminder():
  setDay = int(input("set the day"))
  setHour = int(input("set the hour"))
  setMinute = int(input("set the minutes"))
  x = datetime.datetime(2018,8,setDay,setHour,setMinute,0)
  print(x)
  y = input("ok?")
  if y == "y":
    print("ok")
  elif y == "n":
    z = input("change?")
    if z == "y":
      setReminder()
    else:
      print("ok")
  else:
    print("ok")

setReminder()
