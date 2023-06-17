def make_pretty(func):
    def inner():
        print("I got decorated")
        func() #ordinary
    return inner
def ordinary():
    print("I am ordinary")
@make_pretty #mathd 2 of decorating
def extraordinary():
    print("I am extraordinary")

if __name__=='__main__':
    ordinary()
    print('***************')
    pretty=make_pretty(ordinary)#Method1 of decoration
    pretty()
    print('***************')
    extraordinary()#make_pretty(extraordinary)
    print('***************')