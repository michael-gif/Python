# simple game of hangman
# don't use words with double letters

import random
hiddenWords = ["hello","bye","morning"]
word = random.choice(hiddenWords)
guessLeft = len(word)
lettersLeft = len(word)
guessedLetters = []
print("guess left: " , guessLeft)
def guessWord():
  global lettersLeft, guessLeft, word
  if guessLeft != 0:
    if lettersLeft != 0:
      global guessedLetters
      guess = input("guess a letter in the word or the word itself")
      if guess == word:
        print("you guessed the word")
      elif guess in word:        
        if guess not in guessedLetters:
          print("correct")
          guessedLetters.append(guess)
          lettersLeft -= 1
          guessWord()
        else:
          print("letter already guessed")
          guessLeft -= 1
          print("guess left: " , guessLeft)
          guessWord()      
      else:
        print("wrong")
        guessLeft -= 1
        print("guess left: " , guessLeft)
        guessWord()
    else:
      print("you guessed all the letters")
      print("the word was: " + word)
  else:
    print("no more guesses left. game over")
    print("the word was " + word)
    
guessWord()
