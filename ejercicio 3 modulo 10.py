N = int(input())
s = []
t = []
imc = []
top = []

for i in range(1,N+1):
    s.append(input())

for j in s:
    j = j.split(", ")
    for z in range(1,5):
        j[z] = float(j[z])
    t.append(j)

for w in t:
    imc.append(round(w[1]/(w[2]**2),1))

for o in range (0,N):
    if imc[o]>25 and t[o][3]>100 and t[o][4]>150:
        top.append([t[o][0],imc[o]])

top.sort(key = lambda x: (x[1],x[0]), reverse = True)

for k in top:
    print(f"{top.index(k)+1} {k[0]} {k[1]}")
