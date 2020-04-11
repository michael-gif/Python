# this script works best in repl.it (online ide)
# it's supposed to make you feel like you are hacking, hollywood style

from termcolor import cprint as c
from termcolor import colored
import replit
import time
paulh = ["MailA: hello","MailB: hi","MailC: yep","MailD: nothing here"]
bob3 = ["MailA: yep","MailB: still nothing","MailC: unlucky","MailD: empty user here"]
hoolianJayzam = ["MailA: nah dawg nothing here still"]
notAHacker = ["MailA: Payment for Services"]
MailA = ["to paul: hello.","to bob3: hello.","to hollian: nope","fishy stuff"]
MailB = ["another one to paul: hi","hi bob, nothing here"]
MailC = ["paul, le nope","you lost dude"]
MailD = ["paul, your an idiot.","bob ur empty"]
users = [paulh,bob3,hoolianJayzam,notAHacker]
replit.clear()
username = input(colored("to start the game, enter a username","cyan"))
password = input(colored("and enter a password as well","cyan"))
c("Welcome to  CypherLink, " + username ,"green")
c("cl.software state: v01","green")
c("type cl.help to begin","green")
userconnect = username
def play():
  global userconnect,paulh,users
  Mail = "ABCD"
  command = input(colored("~cl.local." + userconnect + "~","red"))
  if command == "cl.help":
    c("commands:\ncl.help\nrc-check\nrc-connect\nfList","green")
  elif command == "rcheck":
    c("<>local.cl.users-contents=paulh,bob3,hoolianJayzam,notAHacker","green")
  elif command == "rconnect":
    rconnect = input(colored("<>local.connect-","green"))
    if eval(rconnect) in users:
      c("<>connecting...","green")
      time.sleep(1.5)
      c("<>connected to: " + rconnect,"green")
      userconnect = rconnect
    else:
      c("<>user not found","yellow")
  elif command == "fList":
    for x in range(len(users)):
      if users[x] == eval(userconnect):
        c(", ".join(users[x]),"green")
  elif command == "exit":
    if userconnect != username:
      c("<>exiting...","green")
      time.sleep(.5)
      userconnect = username
    else:
      c("<>cannot exit","green")
  elif command == "mail":
    mailcommand = input(colored("<>user.mail.IDletter=","green"))
    for j in Mail:
      if j == mailcommand:
        for gh in range(len(users)):
          if users[gh] == eval(userconnect):
            if mailcommand == "A":
              if j + 1 <= max(MailA):
                c(MailA[gh],"green")
            elif mailcommand == "B":
              if j + 1 <= max(MailB):
                c(MailB[gh],"green")
            elif mailcommand == "C":
              if j + 1 <= max(MailC):
                c(MailC[gh],"green")
            elif mailcommand == "D":
              if j <= max(MailD):
                c(MailD[gh],"green")
  play()
play()
