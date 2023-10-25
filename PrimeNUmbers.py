i = 320432

def forLoop(i):
    for j in range(2, i):
        if(i%j==0):
            return 0
    return 1

while True:
    returned = forLoop(i)
    if(returned == 1):
        f = open("PN.txt", 'a')
        f.write(", " + str(i))
        f.close()
        print(i)
        i += 1
    else:
        i += 1
        continue