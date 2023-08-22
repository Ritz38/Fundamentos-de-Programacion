def separar(seta):
    teta = []

    for jime in seta:

        jime = jime.split(" ")

        teta.append(jime)

    return teta
N = int(input())
n = []







for i in range(1,N+1):
    n.append(input())
n = separar(n)
tata = []







for j in n:
    if j[2]=="positiva":
        tata.append(j)
for x in tata:
    x[2] = x[2].upper()










for z in tata:
    z = z.remove(z[0])













for f in tata:
    f[0] = int(f[0])
    f[2] = int(f[2])
tata.sort(key = lambda x: (x[2], x[0]), reverse = True)


















for ua in tata:
    ua[0] = str(ua[0])
    ua[2] = str(ua[2])
    ua = " ".join(ua)
    print(ua)

















