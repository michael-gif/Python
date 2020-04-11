# failed attempt at making a chat server

from threading import Thread
import time
import random

gamertags = ["andyaustin08","Anquila1978","ArgoOrdie","AspyreFTW","Beecher37","Beezerk","betweentheeyez2","Bilbosmeggins","Howitzer44","hurlock71","Icarus7781","im_DDawg","IMO17","inovashn","PhraseUniverse99","PICHON617","piedudeaus","pikechampion98","PMGS247","pnk667","PopDon","run4roses","RushieNo","Saitothagon","sarahlou33","scarpacci","XtremeFury","r3anyline","YANTROPOV","yellow49","artbru14","zamo1975","Zamo","HE_MAC_33","wazmac","TheRoooster","TheTwizzler1974","ticl","emmonsh"]
messages = ["hi","hello","how are you","sotp","stoop","tsop"]

def func1():
  global gamertags, messages
  while True:
    gamertag = random.choice(gamertags)
    print(gamertag + ": " + random.choice(messages))
    nextmessagesleeptime = random.uniform(0,1)
    time.sleep(nextmessagesleeptime)

def func2():
  username = "Skeppy"
  command = input("")
  print(username + ": " + command)
  func2()

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
