from random import randint

N = int(input())

for i in range(1,N+1):
    vs = input()
    s = vs.split(" ")
    s.pop(0)
    s[0] = int(s[0])
    s = s[0]
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    res = dado1+dado2
    if res>s:
        print("Gana el humano")
    elif res<s:
        print("Gana la plataforma")
    else:
        print("Empate")
    

