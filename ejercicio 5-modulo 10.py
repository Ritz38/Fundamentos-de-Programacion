N = int(input())
s = []
t = []
r = []
for i in range(1,N+1):
    L = int(input())
    for j in range(1, L+1):
        s.append(input())
    for z in range(0,L):
        for u in range(0,L):
            if u != L-1:
                if z == u or u == (L-z-1):
                    a = "#"
                elif (u == (L//2) or z == (L//2)) and z!=u:
                    a = "+"
                else:
                    a = "0"
            elif u==L-1:
                if z == u or u == (L-z-1):
                    a = "#"
                elif (u == (L//2) or z == (L//2)) and z!=u:
                    a = "+"
                else:
                    a = "0"     
            t.append(a)
        r.append(t)
        t = []
    for m in range(0,L):
        r[m] = "".join(r[m])
    if r == s:
        print("Bandera britanica")
    else:
        print("Ni idea")
    r = []
    s = []
