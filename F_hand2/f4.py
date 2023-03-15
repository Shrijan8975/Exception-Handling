with open("file1.txt", "w+") as fp:
    fp.write("1 - First line\n")
    fp.write("2 - Second line\n")
    fp.write("3 - Third line\n")
    fp.seek(0,0)
    data = fp.read()
    print(data)