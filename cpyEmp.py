infile=open(r'./../Data/newemp.csv','r')
outfile=open(r'./../Data/newempCopy.csv','w')

outfile.write(infile.read())
