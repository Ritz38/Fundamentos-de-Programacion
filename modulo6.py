p=[]
cont=0
for i in range(2000):
    x=int(input())
    if x==0:
        break
    p+=[x]
for j in range(len(p)):
    y=1995-p[j]
    if y in p:
        cont=cont+1
print(cont//2)


