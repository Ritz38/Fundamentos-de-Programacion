N = int(input())
s = []
s1 = []
t = []
dic = {}

for i in range(1,N+1):
    s.append(input())

M = int(input())

for j in range(1, M+1):
    t.append(input())


for z in s:
    s1.append(z.split(" "))

for w in s1:
    dic[w[0]]=w[1]
for o in t:
    if (o in dic) ==True:
        print(dic[o])
    else:
        print("palabra no encontrada")

