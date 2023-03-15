with open("file1.txt", "r+") as fp:
    fp.write("11 - First line\n")
    fp.write("22 - Second line\n")
    fp.write("33 - Third line\n")
    fp.seek(0,0)
    data = fp.read()
    print(data)