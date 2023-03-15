#fp = open("file1.txt", "w")
#fp.close()

with open("file1.txt", "w") as fp:
    fp.write("One\n")
    fp.write("Two\n")
    fp.write("Three\n")
    