from datetime import datetime

N = int(input())

suma = 0
cont = 0
for i in range(1,N+1):
    s=input().split(", ")
    s[0] = datetime.strptime(s[0],"%Y-%m-%d")
    s[2] = datetime.strptime(s[2],"%H:%M:%S")
    s[3] = datetime.strptime(s[3],"%H:%M:%S")
    if s[1] == "barberia":
        cont += 1
        p = s[3]-s[2]
        suma += (p.days*24*60*60)+p.seconds+(p.microseconds/60)

res = suma/cont

print(f"{cont} veces")
print(f"{int(res//3600)} horas, {int((res%3600)//60)} minutos, {int((res%3600)%60)} segundos")
