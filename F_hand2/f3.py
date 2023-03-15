with open("file1.txt", "r") as fp:
    print(fp.tell())

    fp.seek(5,0)
    print(fp.tell())