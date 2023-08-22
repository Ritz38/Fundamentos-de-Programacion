N = int(input())
s = []
t = []
dic = {}

for i in range(1,N+1):
    s.append(input())

for j in s:
    t.append(j.split(": "))

for z in t:
    z[1] = int(z[1])

for w in t:
    dic[w[0]] = 0

for r in dic:
    for k in t:
        if r==k[0]:
            dic[r] += k[1]


maximo = 0
ganador = "si"
for n in dic:
    if dic[n]>maximo:
        maximo= dic[n]
        ganador = n

print("El vendedor del mes es",ganador)


    
        


