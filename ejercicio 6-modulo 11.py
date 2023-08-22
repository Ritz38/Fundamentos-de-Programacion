from datetime import datetime
N = int(input())

for i in range(1, N+1):
    s = input().split(" ")
    na = datetime.strptime(s[0],"%Y/%m/%d")
    cont = 0
    for j in range(na.year+1,na.year+int(s[1])+1):
        if datetime(j,na.month,na.day).weekday()==0:
            cont += 1
    print(cont)    
    
    
