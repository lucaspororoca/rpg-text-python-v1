import character
import random

elmo1 = ""
elmo2 = ""

peitoral1 = ""
peitoral2 = ""

arma1 = ""
arma2 = ""

def ExibirItem():
    global elmo1
    global elmo2
    global peitoral1
    
    print(f'{elmo1}')
    print(f'{elmo2}')
    print("")
    print(f'{peitoral1}')
    print(f'{peitoral2}')
    print("")
    print(f'{arma1}')
    print(f'{arma2}')

def AdicionarItem(nomeItem, tipoItem):
    global elmo1
    global elmo2
    global peitoral1
    global peitoral2
    global arma1
    global arma2

    if tipoItem == "Elmo":
        if nomeItem == "Tiara de Cobre":
            elmo1 = nomeItem + " | PESO: 0.5Kg"
            elmo2 = "INT: (+1)"
            character.intelecto += 1
            character.capacidade -= 0.5
        
        if nomeItem == "Tiara de Ferro":
            elmo1 = nomeItem + " | PESO: 0.5Kg"
            character.intelecto += 2
            character.capacidade -= 0.5
        
        if nomeItem == "Tiara de Aço":
            elmo1 = nomeItem + " | PESO: 0.5Kg"
            character.intelecto += 3
            character.capacidade -= 0.5

        if nomeItem == "Elmo de Couro":
            elmo1 = nomeItem + " | PESO: 2.5Kg"
            elmo2 = "DEF: (+1)"
            character.defesa += 1
            character.capacidade -= 2.5
        
        if nomeItem == "Elmo de Ferro":
            elmo1 = nomeItem + " | PESO: 2.5Kg"
            character.defesa += 2
            character.capacidade -= 2.5
        
        if nomeItem == "Elmo de Aço":
            elmo1 = nomeItem + " | PESO: 2.5Kg"
            character.defesa += 3
            character.capacidade -= 2.5

    if tipoItem == "Peitoral":
        if nomeItem == "Peitoral de Couro":
            peitoral1 = nomeItem + " | PESO: 3.5Kg"
            peitoral2 = "DEF: (+3)"
            character.defesa += 3
            character.capacidade -= 3.5

        if nomeItem == "Peitoral de Malha":
            peitoral1 = nomeItem + " | PESO: 4.5Kg"
            character.defesa += 5
            character.capacidade -= 4.5

        if nomeItem == "Peitoral de Ferro":
            peitoral1 = nomeItem + " | PESO: 5.5Kg"
            character.defesa += 7
            character.capacidade -= 5.5
        
        if nomeItem == "Peitoral de Aço":
            peitoral1 = nomeItem + " | PESO: 6.5Kg"
            character.defesa += 9
            character.capacidade -= 6.5
    
    if tipoItem == "Arma":
        if nomeItem == "Varinha de Madeira":
            arma1 = nomeItem + " | PESO: 0.3Kg"
            arma2 = "INT: (+3)"
            character.intelecto += 3
            character.capacidade -= 0.3

        if nomeItem == "Varinha de Madeira":
            arma1 = nomeItem + " | PESO: 0.3Kg"
            arma2 = "INT: (+3)"
            character.intelecto += 3
            character.capacidade -= 0.3

        if nomeItem == "Espada Curta de Ferro":
            arma1 = nomeItem + " | PESO: 7Kg"
            arma2 = "FOR: (+5)"
            character.forca += 5
            character.capacidade -= 7.0
        
        if nomeItem == "Espada Curta de Aço":
            arma1 = nomeItem + " | PESO: 12Kg"
            arma2 = "FOR: (+7)"
            character.forca += 7
            character.capacidade -= 12.0

        if nomeItem == "Espada Curta de Platina":
            arma1 = nomeItem + " | PESO: 22Kg"
            arma2 = "FOR: (+11)"
            character.forca += 11
            character.capacidade -= 22.0

def GerarItem():
    a = random.randrange(1,3)

    #if a == 1:
        