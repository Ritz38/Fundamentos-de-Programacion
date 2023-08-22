N = int(input())
s = []
t = []
dic = {"enero":13,"febrero":14,"marzo":3,"abril":4,"mayo":5,"junio":6,"julio":7,"agosto":8,"septiembre":9,"octubre":10,"noviembre":11,"diciembre":12}
dias = {0:"sabado",1:"domingo",2:"lunes",3:"martes",4:"miercoles",5:"jueves",6:"viernes"}

for i in range(1,N+1):
    s.append(input())

for j in s:
    t.append(j.split("-"))

for z in t:
    z[0] = float(z[0])
    if z[1]!="enero" and z[1]!="febrero":
        z[2] = float(z[2])
    else:
        z[2] = float(z[2])-1
    z[1] = float(dic[z[1]])

for w in t:
    zeller = int((w[0]+((13*(w[1]+1))//5)+w[2]+(w[2]//4)-(w[2]//100)+(w[2]//400))%7)
    print(dias[zeller])




