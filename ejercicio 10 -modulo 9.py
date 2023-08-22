x = open("conversaciones.txt","r")

for  i in x:
    i = i.replace("\n","")
    i = i.lower()
    fa = ["sin embargo","no obstante","ahora bien","aun asi"]
    te = ["por tanto","dado que","por consiguiente","asi pues","por ende"]
    cont = 0
    for k in fa:
        if k in i:
            cont += 1*(i.count(k))
    cont1 = 0
    for c in te:
        if c in i:
            cont1 += 1*(i.count(c))
    print(f"Opositivos {cont} Causativos {cont1}")
    
    
