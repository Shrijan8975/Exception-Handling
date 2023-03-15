with open("file1.txt", "r") as fp:
    x = fp.tell()
    print(x)

    fp.read(5)
    print(fp.tell())
    fp.read()
    print(fp.tell())