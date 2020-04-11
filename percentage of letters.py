# this is letter frequency

sentence = input("Enter something here.")
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sentence = sentence.lower()
lengthofsentence = 0
for x in range(len(sentence)):
  if sentence[x].isalpha() == True:
    lengthofsentence += 1
    for y in range(26):
      if sentence[x] == alphabet[y]:
        values[y] += 1
for z in range(25):
  if values[z] != 0:
    percentage = values[z]/lengthofsentence
    percentage = percentage*100
    print(alphabet[z] , ":" , percentage)
