#built in modules
# 1.
import math
print(dir(math))
print(math.factorial(5))
print(math.sqrt(25))

# 2.
import random
print(random.random())
print(random.randint(1,20))
print(random.sample(range(1,100),37))

# some important modules - os, sys, re, requests, csv

# 3.
import os
dir(os)
print(os.getcwd())
print(os.mkdir('sample'))
print(os.rmdir('sample'))
print(os.chdir('.\..\..\project1\Programs'))
res = os.walk(r'C:\Users\nehal\PycharmProjects\project1')
print(res)
for each in res:
    print(each)

# Three ways of importing modules
# import modulename
   # import math
# from modulename import funct_name
   # from math import factorial,sqrt
        # factorial(5)
        # sqrt(9)
   # from math import *
# import modulename as objname(any name can be given as a object)
   # import math as m