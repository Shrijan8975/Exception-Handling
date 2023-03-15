fp =  open("f1.txt", "a")

data = ""
while(data != "$"):
    data = input("Enter Data: ")
    if(data != "$"):
        fp.write(data)
        fp.write("\n")

fp.close()