infile=open(r'.\..\Data\file1.txt','r')
print(infile.read())
print("------------------------------------")
print(infile.seek(0))
print(infile.read())
print("------------------------------------")
print(infile.seek(0))
print(infile.readline())
print(infile.readline())
print(infile.read())
print("------------------------------------")
print(infile.seek(0))
print(infile.readlines())
