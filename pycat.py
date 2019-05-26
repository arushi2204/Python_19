import sys


file_name=sys.argv[1]


f=open(file_name)
 

for i in f:
    print(i,end='')
