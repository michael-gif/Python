# picks a random name (the names were from a random name generator)

import random
import time
num = random.randint(0,29)
names = ['Sherlyn Borkowski','Monserrate Pepin','Cora Brogdon','Elise Sollars','Holly Marcinek','Hee Inniss','Halina Laroche','Lorrine Eastland','Lorinda Butler','Shan Chabot','Tiffani Heimbach','Tammara Sinclair','Lyda Figueras','Carri Lisk','Shelba Geoghegan','Jessenia Penney','Keneth Durney','Xochitl Underdown','Eun Gunnells','Ayanna Seguin','Leighann Delgadillo','Omer Sutterfield','Britni Wurtz','Calvin Waddell','Merri Holeman','Kourtney Mikel','Julee Trusty','Chery Nogle','Sherman Hommel','Ocie Casillas']
randNames = random.randint(5,10)
for x in range (0,randNames):
  print(random.choice(names), end= "\r")
  time.sleep(0.05)

print(names[num])
