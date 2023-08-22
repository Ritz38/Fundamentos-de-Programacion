from datetime import datetime

N = int(input())
dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for i in range(N):
    s = datetime.strptime(input(),"%d/%m/%Y")
    print("lun","mar","mie","jue","vie","sab","dom",sep="\t")
    if (s.year%4==0 or s.year%400==0) and s.year%100!=0 and (s.month==2):
        r = dic[s.month]+1
    else:
        r = dic[s.month]

    for j in range(1,r+1):
        for z in range(0,7):
            if datetime(s.year,s.month,j).weekday()==z and j==1:
                if z!=0:
                    print("\t"*(z-1),end="\t")
                if datetime(s.year,s.month,j).weekday()==6:
                    print(j,end="")
                else:
                    print(j,end="\t")
                break
            elif datetime(s.year,s.month,j).weekday()==z and j!=1 and j!=r:
                if datetime(s.year,s.month,j).weekday()==6:
                    print(j,end="")
                else:
                    print(j,end="\t")
                break
            elif datetime(s.year,s.month,j).weekday()==z and j==r:
                if datetime(s.year,s.month,j).weekday()==6:
                    print(j,end="")
                else:
                    print(j)
                break
        if datetime(s.year,s.month,j).weekday()==6:
            print()
    print()
    
    
        
        
        
        
