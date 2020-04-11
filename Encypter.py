# i believe this works best when using repl.it (the online ide for python and other languages)

from progressbar import *               # just a simple progress bar
import time

widgets = ['Test: ', ' ', Bar(marker='#',left='|',right='|'), ' ', ETA(), ' ', FileTransferSpeed()] #see docs for other options

pbar = ProgressBar(widgets=widgets, maxval=500)
'''pbar.start()

for i in range(500):
    time.sleep(.01)
    pbar.update(i) #this adds a little symbol at each iteration
pbar.finish()'''

def encryptdecrypt():
  i = 0
  command = input("press e for encrypt, press d for decrypt")
  if command == "e":
    ptext = input("")
    ctext = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!:;?/#" 
    cipher = "QmXV#sNyAMog,FfiOCn bBrYHLlPUqkR:vtuEpQ.Sxd!JDeZGh/wTaK;cIjz"
    pbar = ProgressBar(widgets=widgets, maxval=len(ptext)*60)
    pbar.start()
    for x in range(len(ptext)):
      for y in range(60):
        if ptext[x] == alphabet[y]:
          ctext.append(cipher[y])
          i += 1
          time.sleep(.025)
          pbar.update(i)
    pbar.finish()
    print("".join(ctext))
  elif command == "d":
    ctext = input("")
    ptext = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!:;?/#" 
    cipher = "QmXV#sNyAMog,FfiOCn bBrYHLlPUqkR:vtuEpQ.Sxd!JDeZGh/wTaK;cIjz"
    pbar = ProgressBar(widgets=widgets, maxval=len(ctext)*60)
    pbar.start()
    for x in range(len(ctext)):
      for y in range(60):
        if ctext[x] == cipher[y]:
          ptext.append(alphabet[y])
          i += 1
          time.sleep(.025)
          pbar.update(i)
    pbar.finish()
    print("".join(ptext))

encryptdecrypt()
