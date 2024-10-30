a=input()
b=input()### convert to int 
c=input()
if int(a) < int(b):
    a=b
if int(a) < int(c):
    a=c

print(a)
