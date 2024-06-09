a=int(input('Ente age 1='))
b=int(input('Ente age 2='))
c=int(input('Ente age 3='))
if ((a>b) and (a>c)):
    print("a is older =",a)
elif (a<b and a<c):
    print("a is smaller",a)
if(b>c and b>a):
    print("b is older =",b)
elif(b<a and b <c):
    print("b is smaller =",b)
if(c>a and c <b):
    print('c is older =',c)
elif(c<a and c<b):
    print('c is smaller =',c)
