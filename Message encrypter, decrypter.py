# Coded in Python

'''
This message encrypter and decrypter can encrypt and decrypt messages, even if they have a space in them. It uses a changeable cipher.
The decrypter just has the cipher and alphabet swapped around. So the already encrypted message gets encrypted into the regular alphabet
using the cipher as the alphabet.
'''


###########################################################################################################################################


#encrypter:


alphabet = "abcdefghijklmnopqrstuvwxyz" 
cipher = "msyogfinbrlqkvtupxdehwacjz"
word = input("enter word/sentence to be encrypted")
newWord = []
i = 0
j = 0

def select():
  selection = input("Enter '1' run code \nEnter '2' to change the cipher, then run the code")
  if selection == "1":
    encrypt()
  elif selection == "2":
    changeCipher()
  else:
    print("wrong answer")

def changeCipher():
  global cipher
  cipher = input("enter new cipher")
  encrypt()

def encrypt():
  global i, j
  if j == 25:
    j = 0
    encrypt()
  else:
    if i >= len(word):
      print(word + ":" + "\n" + ''.join(newWord))
    else:
      if word[i].isalpha() == True:
        if word[i] == alphabet[j]:
          newWord.append(cipher[j])
          i += 1
          j += 1
          encrypt()
        else:
          j += 1
          encrypt()
      else:
        i += 1
        encrypt()

select()

###########################################################################################################################################


#decrypter:


alphabet = "msyogfinbrlqkvtupxdehwacjz" 
cipher = "abcdefghijklmnopqrstuvwxyz"
word = input("enter word/sentence to be decrypted")
newWord = []
i = 0
j = 0
def select():
  selection = input("Enter '1' run code \nEnter '2' to change the cipher, then run the code")
  if selection == "1":
    encrypt()
  elif selection == "2":
    changeCipher()
  else:
    print("wrong answer")

def changeCipher():
  global cipher
  cipher = input("enter new cipher")
  encrypt()

def encrypt():
  global i, j
  if j == 25:
    j = 0
    encrypt()
  else:
    if i >= len(word):
      print(word + ":" + "\n" + ''.join(newWord))
    else:
      if word[i].isalpha() == True:
        if word[i] == alphabet[j]:
          newWord.append(cipher[j])
          i += 1
          j += 1
          encrypt()
        else:
          j += 1
          encrypt()
      else:
        i += 1
        encrypt()

select()
