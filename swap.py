import os

File1 = input("Input file 1 name:")
File2 = input("Input file 2 name:")

with open(file1, 'r') as a:
    data_a=a.read()

with open(file2, 'r') as b:
    data_b=b.read()

with open(File1, 'w') as b:
    a.write(data_b)

with open(File2, 'w') as a:
    a.write(data_a)