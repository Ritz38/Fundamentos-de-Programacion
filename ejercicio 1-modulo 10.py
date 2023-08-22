def separar(s):
    t = []
    for j in s:
        j = j.split(" ")
        t.append(j)
    return t

N = int(input())
s = []

for i in range(1,N+1):
    s.append(input())

s = separar(s)
t = []

for j in s:
    if j[2]=="positiva":
        t.append(j)

for z in t:
    z[2] = z[2].upper()

for w in t:
    w = w.remove(w[0])

for o in t:
    o[0] = int(o[0])
    o[2] = int(o[2])

t.sort(key = lambda x: (x[2], x[0]), reverse = True)

for u in t:
    u[0] = str(u[0])
    u[2] = str(u[2])
    u = " ".join(u)
    print(u)

