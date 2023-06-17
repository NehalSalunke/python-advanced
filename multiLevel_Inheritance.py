class A:
    def whoami(self):
        print('I am in A')
class B(A):
    def whoami(self):
        print('I am in B')
class C(A):
    def whoami(self):
        print('I am in C')
class D(B,C):
    pass

d1 =D()
d1.whoami()