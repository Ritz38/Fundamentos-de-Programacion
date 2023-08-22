def zaza(f):
    resultado=[]
    for k in range(0,len(f),10):
        numeros=[]
        for numero in range(0,10,2):
            numeros.append(f[k+numero])
        numeros.sort()
        if f[k+1]==f[k+3] and f[k+1]==f[k+5] and f[k+1]==f[k+7] and f[k+1]==f[k+9]:
            if numeros[0]=="10" and numeros[1]=="11" and numeros[2]=="12" and numeros[3]=="13" and numeros[4]=="14":
                resultado.append("Escalera real")
            elif int(numeros[0])==int(numeros[1])-1 and int(numeros[0])==int(numeros[2])-2 and int(numeros[0])==int(numeros[3])-3 and int(numeros[0])==int(numeros[4])-4:
                resultado.append("Escalera de color")
            else:
                resultado.append("Color")
        else:
            if int(numeros[0])==int(numeros[1])-1 and int(numeros[0])==int(numeros[2])-2 and int(numeros[0])==int(numeros[3])-3 and int(numeros[0])==int(numeros[4])-4:
                resultado.append("Escalera normal")
            else:
                resultado.append("Otra mano")
    return resultado
        
M=int(input())
m=[]
for i in range(M*10): 
    m.append(str(input()))
x=zaza(m)
for h in range(len(x)):
    print(x[h])



