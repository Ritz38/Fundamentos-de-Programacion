N = int(input())
s = []

for i in range(1, N+1):
    t = []
    for j in range(0, 5):
        s.append(input())
    s.pop(0)
    for z in s:
        t.append(z.split(" "))
        for w in t:
            w[0] = int(w[0])
            w[1] = int(w[1])
            w[2] = int(w[2])
            w[3] = int(w[3])
    r = (t[0][0]+t[1][1]+t[2][2]+t[3][3])
    m = (t[0][3]+t[1][2]+t[2][1]+t[3][0])
    if r==m:
        y =  True
    else:
        y = False

    x = []
    suma = 0
    for k in t:
        for l in k:
            suma += l
        x.append(suma)
        suma = 0
    p = []
    suma1 = 0
    for f in t:
        for h in f:
            suma1 += h
        p.append(suma1)
        suma1 = 0

    cont = x[0]
    for mi in range(0,4):
        if x[mi]==r  and p[mi]==m and p[mi]==x[mi] and x[mi]==cont:
            secur = True
        else:
            secur = False
        cont = x[mi]

    if (secur == True) and (y == True):
        print("Cuadrado magico")
    else:
        print("Cuadrado muggle")
    
    s = []
