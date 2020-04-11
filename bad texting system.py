# supposed to be a texting system
# it doesn't work becuase it doesn't use a server or anything

people = ['Joelle Barthel','Nery Roseman','Assunta Rittenhouse','Antione Fricke','Minta Hesse']

person = input("Type the peron you want to message")
packet = []
message = ""
for x in range(len(people)):
  if person == people[x]:
    packet.append(people[x])
    message = input("Type the message you want to send")
    packet.append(message)
    print(" ID: " , x , ", " , people[x] , "\n" , "Message: " , message)
    print(packet)
    break
  else:
    if x != len(people) - 1:
      print("Searching...")
    elif x == len(people) - 1:
      print("There is no contact called " + person)

####################################################################

people = ['Joelle Barthel','Nery Roseman','Assunta Rittenhouse','Antione Fricke','Minta Hess']
receiveMessage = packet
def receivepacket():
  if receiveMessage[0] in people:
    print(" Message from: " , receiveMessage[0] , "\n" , receiveMessage[1])
  else:
    print(" Message from: Unknown" , "\n" , receiveMessage[1])
receivepacket()
