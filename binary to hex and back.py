def binaryhex():
  binarytranslate = [8,4,2,1]
  inputword = input("1 for bin-hex, 2 for hex-bin")
  letters = ["A","B","C","D"]
  if inputword == "1":
    binary = input("")
    hexleft = 0
    hexright = 0
    for x in range(8):
      if x < 4:
        if binary[x] == "0":
          hexleft += 0
        else:
          hexleft += binarytranslate[x]
      else:
        if binary[x] == "0":
          hexright += 0
        else:
          hexright += binarytranslate[x-4]
      if hexleft > 9:
        hexleft = letters[hexleft-10]
      if hexright > 9:
        hexright = letters[hexright-10]
    print(hexleft,hexright)
    binaryhex()
  elif inputword == "2":
    print()
    binaryhex()
  else:
    print()
    binaryhex()
binaryhex()
