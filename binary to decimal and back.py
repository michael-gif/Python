def binarydecimal():
  binarytranslate = [128,64,32,16,8,4,2,1]
  word = input("1 for binary to decimal, 2 for decimal to binary")
  if word == "1":
    binary = input("")
    decimalconversion = 0
    for x in range(8):
      if int(binary[x]) == 0:
        decimalconversion += 0
      else:
        decimalconversion += binarytranslate[x]
    print(decimalconversion)
    binarydecimal()
  elif word == "2":
    decimal = int(input(""))
    binaryconversion = []
    for y in range(8):
      if decimal >= binarytranslate[y]:
        binaryconversion.append(1)
        decimal = decimal - binarytranslate[y]
      else:
        binaryconversion.append(0)
    print("".join(map(str, binaryconversion)))
    binarydecimal()
  else:
    print("invalid")
    binarydecimal()

binarydecimal()
