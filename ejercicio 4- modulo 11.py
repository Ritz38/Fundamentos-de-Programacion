from datetime import datetime

C = int(input())

for i in range(1,C+1):
    s = datetime.strptime(input(),"%I:%M:%S %p")
    tiempo = s.second + (s.minute*60) + (s.hour*3600)
    porcentaje = round((tiempo*100)/86400,3)
    print(f"Loading day ... {porcentaje}%")
