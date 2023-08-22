talleres=[9,11,12,8,12,9,11,8,11,10,9,10]
notas=[]
resultado=[]
N=int(input())
for i in range(N):
    x=input()
    x=x.split(", ")
    notas.append(x)
for j in notas:
    for i in range(len(j)):
        j[i] = int(j[i])
for l in notas:
    promedio=0
    rr=[]
    for f in range(1,len(l)):
        promedio+=(round(((l[f]/talleres[f-1])*5),1))
    promedio=round((promedio)/12,1)
    rr.append(l[0])
    rr.append(promedio)
    resultado.append(rr)
resultado.sort(key=lambda x: x[0])
for e in resultado:
    print(e[0], e[1])
