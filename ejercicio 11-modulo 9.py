x =  open("trifelios.txt","r")

for j in x:
    j = j.replace("\n","")
    s = j.split("-")
    verdad = False
    for c in s[0]:
        u = []
        for z in range(s[0].find(c)-len(s[0])+1,s[0].find(c)+1):
            u.append(s[0][z])
        u = "" . join(u)
        if u == s[1]:
            verdad = True
         
    if verdad==True:
        print("Es trifelio")
    else:
        print("No es trifelio")
