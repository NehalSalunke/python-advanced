def mysum(a,b):
    return a+b
def mysub(a,b):
    return(a-b)
def mymul(a,b):
    return a*b
def mydiv(a,b):
    return a/b

print(__name__)
if __name__=='__main__':
    print(mysum(5,6))
    print(mysub(5,3))
    print(mymul(4,9))
    print(mydiv(8,2))