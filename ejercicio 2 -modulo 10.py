N = int(input())
s = []
t = []
p = []
k = []
n = []
resultados = []
ejercicios = {1:9,2:11,3:12,4:8,5:12,6:9,7:11,8:8,9:11,10:10,11:9,12:10}

for i in range(1, N+1):
    s.append(input())

for j in s:
    t.append(j.split(", "))

for z in t:
    for a in range(0,13):
        if z[a] == z[0]:
            z[a] = int(z[a])
        else:
            z[a] = float(z[a])

for w in t:
    for e in range(1,13):
        suma = round((w[e]/ejercicios[e])*5,1)
        p.append(suma)
    promedio = 0
    for ñ in p:
        promedio += ñ
    promedio = round(promedio / len(p),1)
    resultados.append([w[0],promedio])
    p = []

resultados.sort(key = lambda x: x[0])

for l in resultados:
    print(l[0],l[1])




