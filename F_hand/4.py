from os import path

if(path.exists("f1.txt")):
    fp =  open("f1.txt", "r")
    for line in fp:
        print(line.strip())
    fp.close()
else:
    print("File Not found...")