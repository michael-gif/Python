import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
newalphabet = []
print(''.join(alphabet))
for x in range(26):
    num = random.randint(0,len(alphabet)-1)
    newalphabet.append(alphabet[num])
    alphabet.pop(num)
print(''.join(newalphabet))
