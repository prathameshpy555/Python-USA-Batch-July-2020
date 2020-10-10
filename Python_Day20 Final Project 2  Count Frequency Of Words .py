# WAP accept a file and count frequency of words :
filen = input("Enter a file name : ")
file = open(filen)
print()
lines = file.readlines()
x=file.read()

mydict = {}

for line in lines :
    for item in line.strip().split() :
        if item not in mydict.keys() :
            mydict[item] = 1
        else:
            mydict[item] = mydict[item] + 1

for item in mydict :
    print("{:15} : {}".format(item,mydict[item]))
input()
