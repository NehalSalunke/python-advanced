import csv
infile=open(r'./../Data/newemp.csv','r')
'''abcd=csv.reader(infile)
for each in abcd:
    print(each)
'''
xyz=csv.DictReader(infile)
for each in xyz:
    print(each)