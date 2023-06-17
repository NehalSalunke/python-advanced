# create another list which is nothing but square of each element in first list

#l1=[1,2,3,4,5]
l1=[]
elements=int(input("enter number of elements in list : "))
while len(l1) ==elements:
    ele=int(input("enter element"))
    l1.append(ele)
print(l1)
l2=[]
for each in l1:
    l2.append(each**2)
print(l2)