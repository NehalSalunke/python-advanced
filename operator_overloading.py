class A:
    def __init__(self, geta):
        self.a=geta
    def __add__(self,other):
        return self.a/other.a

#operator overloading
obj1=A(100)
obj2=A(20)
print(obj1+obj2)
#obj1.__add__(obj2) after calling '+' sign call goes to
# __add__ method present in the class A and the method get executed
# if __add__ method was not found in class A then call could have gone to
#__add__ method of system default class and would have been given addition as a output
# we cannot add two objects that's why we created add method to get desired output
# otherwise the objects will get override and it will throw an error 
