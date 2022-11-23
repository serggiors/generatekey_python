import random

def GenerateKey():
    length = random.randrange(8,12)
    key = []
    for x in range(length):
        key.append(chr(random.randrange(33,126)))
    return "". join(key)

PrintGenerateKey = GenerateKey()
print (PrintGenerateKey)