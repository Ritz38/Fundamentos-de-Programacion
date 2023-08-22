d=int(input())
y=0
x=0
for i in range(1,d+1):
    p=float(input()) 
    x=x+y
    y=((i)*p)-x
    print(int(y))

