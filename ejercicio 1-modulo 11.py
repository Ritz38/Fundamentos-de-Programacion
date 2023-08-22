from datetime import datetime
C = int(input())

for i in range(1,C+1):
    s = []
    s.append(input())
    t = []
    d = []
    for j in s:
        t = j.split(" ")
    t.pop(0)
    for z in t:
        a = datetime.strptime(z,"%Y-%m-%d")
        d.append(a)
    diferencia = d[1]-d[0]
    print(f"{diferencia.days} dias = {diferencia.days*24} horas = {diferencia.days*24*60} minutos = {diferencia.days*24*3600} segundos")
    t = []
    
    
        
    
