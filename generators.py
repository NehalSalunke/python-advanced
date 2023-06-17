
### reading other text file
def fetch_lines(filename):
    filename=open(r'./../Data/file1.txt','r')
    for each in filename:
        yield each
read=fetch_lines('file1.txt')
print(read)
for each in read:
    print(each)


###reading value inserted and giving output as square
def sqlist(num):
    for each in num:
       yield each**2
squares=sqlist([1,3,5,7,9])
print(squares)
print(next(squares))
for each in squares:
    print(each)

###reading value inserted by user and giving output as cube

def cubes(num):
    yield  each**3
value=cubes(int(input("enter number ")))
print(value)
print(next(value))
