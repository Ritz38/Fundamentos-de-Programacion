from datetime import datetime
N = int(input())
d = {"true vampires":0,"early birds":0,"sunny warmers":0,"lunch workers":0,"sunset lovers":0,"prime timers":0}

for i in range(1,N+1):
    s = input()
    a = datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
    if (a.hour<=3):
        d["true vampires"] += 1
    elif (a.hour>=4 and a.hour<=7):
        d["early birds"] += 1
    elif (a.hour>=8 and a.hour<=11):
        d["sunny warmers"] += 1
    elif (a.hour>=12 and a.hour<=15):
        d["lunch workers"] += 1
    elif (a.hour>=16 and a.hour<=19):
        d["sunset lovers"] += 1
    else:
        d["prime timers"] += 1

for j in d:
    print(f"{j} {d[j]}")
