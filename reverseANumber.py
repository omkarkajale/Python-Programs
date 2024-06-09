Value=int(input("Enter the value"))
rev=0
while(Value>0):
    rev=(rev*10)+(Value % 10)
    Value=Value//10
print('The reverse is',rev)