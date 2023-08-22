retiro=int(input())
cincuenta=retiro//50000
veinte=(retiro-(cincuenta*50000))//20000
diez=(retiro-(cincuenta*50000)-(veinte*20000))//10000
cinco=(retiro-(cincuenta*50000)-(veinte*20000)-(diez*10000))//5000
dos=(retiro-(cincuenta*50000)-(veinte*20000)-(diez*10000)-(cinco*5000))//2000
mil=(retiro-(cincuenta*50000)-(veinte*20000)-(diez*10000)-(cinco*5000)-(dos*2000))//1000
if veinte==0 and diez==0 and cinco==0 and dos==0 and mil==0:
    print(cincuenta,"de $50000")
elif veinte==0 and diez==0 and cincuenta==0 and dos==0 and mil==0:
    print(cinco, "de $5000")
elif cincuenta==0 and cinco==0 and dos==0 and diez==0 and veinte==0:
    print(mil, "de $1000")
elif diez==0 and cinco==0 and dos==0 and mil==0:
    print(cincuenta,"de $50000")
    print(veinte, "de $20000")
elif cincuenta==0 and cinco==0 and dos==0 and diez==0:
    print(veinte, "de $20000")
    print(mil, "de $1000")
elif cinco==0 and dos==0 and mil==0:
    print(cincuenta,"de $50000")
    print(veinte, "de $20000")
    print(diez, "de $10000")
elif diez==0 and mil==0:
    print(cincuenta,"de $50000")
    print(veinte, "de $20000")
    print(cinco, "de $5000")
    print(dos, "de $2000")
elif dos==0 and mil==0:
    print(cincuenta,"de $50000")
    print(veinte, "de $20000")
    print(diez, "de $10000")
    print(cinco, "de $5000")
elif mil==0:
    print(cincuenta,"de $50000")
    print(veinte, "de $20000")
    print(diez, "de $10000")
    print(cinco, "de $5000")
    print(dos, "de $2000")
else:
    print(cincuenta,"de $50000")
    print(veinte, "de $20000")
    print(diez, "de $10000")
    print(cinco, "de $5000")
    print(dos, "de $2000")
    print(mil, "de $1000")

