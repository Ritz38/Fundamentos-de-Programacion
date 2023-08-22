from datetime import datetime

N = int(input())

for i in range(N):
    s = input().split(" ")
    inicio = datetime.strptime(s[0],"%d-%m-%Y")
    final = datetime.strptime(s[1],"%d-%m-%Y")
    resta = final-inicio
    c = []
    n = resta.days//5
    for j in range(n):
        c.append("5")
    d = resta.days%5
    for z in range(d):
        c.append("1")
    c1 = " ".join(c)
    print(c1)
