def separar(s):
    t = []
    d = []
    for i in s:
        t.append(i.split())
    
    for j in t:
        for z in j:
            d.append(z)
    return d

N = int(input())
s = []
for i in range(1,N+1):
    s.append(input())

regue = separar(s)
M = int(input())
t = []

for j in range(1,M+1):
    t.append(input())

rock = separar(t)


d = []

for z in regue:
    if (z not in d):
        d.append(z)
x = len (d)

d= []

for w in rock:
    if (w not in d):
        d.append(w)
y = len(d)

print(f"Reggaeton: {x} Rock: {y}")
