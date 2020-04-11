# this decrypter is for a caesar cipher.
# it checks every possible shift for the code, so you need to check all of the outputs.

#code = 'LZWJW SJW GMLOSJV KWUJWLK VWLSADK GX JALMSD SFV KAYFK GX JWUGYFALAGF DACW HSKKOGJVK SFV ZSFVKZSCWK LZWJW SJW SDKG AFOSJV GJ HWJKGFSD KWUJWLK DACW LZW WPHWJAWFUW GX HSKKAFY LZJGMYZ S JALMSD AFALASLAGF GJ OZSL S ESF DWSJFK STGML ZAEKWDX LZJGMYZ TWAFY S ESKGF'
code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
indexes = []
code = code.lower()
for x in range(len(code)):
    if code[x] == ' ':
        indexes.append(' ')
    else:
        for y in range(26):
            if code[x] == alphabet[y]:
                indexes.append(y)
for a in range(26):
    codeguess = []
    for z in range(len(indexes)):
        if indexes[z] != ' ':
            codeguess.append(alphabet[indexes[z]])
            indexes[z] += 1
            if indexes[z] == 26:
                indexes[z] = 0
        else:
            codeguess.append(' ')
    print("".join(codeguess) + "\n")
