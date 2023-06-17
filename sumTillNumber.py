#Calculate the sum of all numbers from 1 to the given number
num = int(input("enter any number between 0-100: "))
addition=0
if num<0 or num>100:
    print("give input in range 1-100")
else:
    for each in range(0,num+1):
        addition=addition+each
    print("The addition of numbers till input is : ", addition)