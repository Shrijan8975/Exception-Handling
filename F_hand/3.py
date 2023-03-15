fp =  open("f1.txt", "r")
for line in fp:
    print(line.strip())
fp.close()