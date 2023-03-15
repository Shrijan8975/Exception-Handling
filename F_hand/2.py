fp =  open("f1.txt", "r")
#data = fp.read()
data = fp.read(12)
print(data)

fp.close()