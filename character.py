import random

nome = ""
classe = 0
raca = 0

forca = 0
defesa = 0
vigor = 0
intelecto = 0
destreza = 0
carisma = 0

def CriarPersonagem(classe1 = 0, raca1 = 0):
    global classe
    global raca
    global forca
    global defesa
    global vigor
    global intelecto
    global destreza
    global carisma
    
    if classe1 == 1:
        classe = "Humano"
    
    if classe1 == 2:
        classe = "Elfo"

    if classe1 == 3:
        classe = "Anão"

    if classe1 == 4:
        classe = "Gnomo"

    if raca1 == 1:
        forca = random.randrange(5,10)
        defesa = random.randrange(10,15)
        vigor = random.randrange(15,20)
        intelecto = random.randrange(0,5)
        destreza = random.randrange(20,25)
        carisma = random.randrange(20,25)

        destreza = destreza * 1.5
        carisma = carisma * 1.3

        print(f'VIG:  {vigor}')
        print(f'FOR:  {forca}')
        print(f'DEF:  {defesa}')
        print(f'INT:  {intelecto}')
        print(f'DES:  {destreza}')
        print(f'CAR:  {carisma}')
