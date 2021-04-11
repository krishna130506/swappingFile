def swapFileData():
        files1 = input("please input the name of the first file: ")
        files2 = input("please input the name of the second file: ")
        with open(files1,'r')as a:
                data_a = a.read()
        with open(files2,'r')as b:
                data_b = b.read()
        with open(files1,'w')as a:
                a.write(data_b)
        with open(files2,'w')as b:
                b.write(data_a)
        print("the files have been swapped")
swapFileData()