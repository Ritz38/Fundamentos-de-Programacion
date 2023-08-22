from random import randint

N = int(input())

for i in range(N):
    p = input().split(" ")
    p.pop(0)
    for j in range(0,10):
        p[j]=int(p[j])
    m = []
    for z in range(0,10):
        m.append(randint(1,13))
    h = 0
    l = 0
    for w in range(0,10):
        if m[w]>p[w]:
            h += 1
        elif p[w]>m[w]:
            l += 1
    print(f"Puntos humano: {h} Puntos plataforma: {l}")
