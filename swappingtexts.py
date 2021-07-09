def fileswap():
    file1=input("What file do you want to swap: ")
    file2=input("What is the other file: ")
   
    with open(file1, 'r') as a:
        data_a=a.read()
    with open(file2, 'r') as a:
        data_b=a.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as a:
        a.write(data_a)
        

fileswap()