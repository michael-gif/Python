# tried making one of the enigma dials

encryptionword = input("")
alphabet = "abcdefghijklmnopqrstuvwxyz"
cypher = ['a','g','o','t','m','u','e','w','v','h','j','n','q','s','d','x','z','f','i','k','c','p','l','y','r','b']
encryptedWord = []
i = 0
j = 0

def shiftCypher():
  cypher.append(cypher[0])
  cypher.remove(cypher[0])
  encrypt()

def encrypt():
  global i, j
  if j == 25:
    j = 0
    encrypt()
  else:
    if i >= len(encryptionword):
      print(encryptionword + ":" + "\n" + ''.join(encryptedWord))
    else:
      if encryptionword[i].isalpha() == True:
        if encryptionword[i] == alphabet[j]:
          encryptedWord.append(cypher[j])
          i += 1
          j += 1
          shiftCypher()
        else:
          j += 1
          encrypt()
      else:
        i += 1
        encrypt()

encrypt()

###########################################################################################################################################

decryptionword = input("")
cypher = "agotmuewvhjnqsdxzfikcplyrb"
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
decryptedWord = []
p = 0
q = 0

def shiftCypher():
  alphabet.insert(0,alphabet[25])
  alphabet.remove(alphabet[25])
  encrypt()

def encrypt():
  global p, q
  if q == 25:
    q = 0
    encrypt()
  else:
    if p >= len(decryptionword):
      print(decryptionword + ":" + "\n" + ''.join(decryptedWord))
    else:
      if decryptionword[p].isalpha() == True:
        if decryptionword[p] == cypher[q]:
          decryptedWord.append(alphabet[q])
          p += 1
          q += 1
          shiftCypher()
        else:
          q += 1
          encrypt()
      else:
        p += 1
        encrypt()

encrypt()
