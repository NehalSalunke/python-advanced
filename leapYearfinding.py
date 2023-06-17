'''take input from user in terms of year
if year is divisible by 4 then it is leap year
above is valid for non century year
if year is century year then condition will be different'''

year=int(input("Enter any year to know more: "))
if year%100==0 and year%400==0:
        print(year,"Yes it is leap year")
elif year%100==0 and year%4==0:
        print(year,"Yes it is leap year")
else:
        print(year, "Not an leap year")
