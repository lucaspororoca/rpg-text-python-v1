import random
import itens
import eventos
import os

classe = 0
raca = 0
acoes = 0
capacidade = 0.0
moedas = 100

forca = 0
defesa = 0
vigor = 0
intelecto = 0 
piedade = 0
destreza = 0
carisma = 0



def CriarPersonagem(nome, classe1, raca1):
    global moedas
    global classe
    global raca
    global acoes
    global capacidade
    global forca
    global defesa
    global vigor
    global intelecto
    global piedade
    global destreza
    global carisma
    
    if classe1 == "1":
        classe = "Guerreiro"
        itens.AdicionarItem("Elmo de Couro", "Elmo")
        itens.AdicionarItem("Peitoral de Couro", "Peitoral")
    
    if classe1 == "2":
        classe = "Mago"
        itens.AdicionarItem("Tiara de Cobre", "Elmo")

    if classe1 == "3":
        classe = "Arqueiro"

    if classe1 == "4":
        classe = "Paladino"

    if raca1 == "1":
        raca = "Humano"
        capacidade += 160
        forca = random.randrange(5,10)
        defesa = random.randrange(10,15)
        vigor = random.randrange(15,20)
        intelecto = random.randrange(0,5)
        piedade = random.randrange(5,10)
        destreza = random.randrange(20,25)
        carisma = random.randrange(20,25)

        destreza = int(destreza * 1.5)
        carisma = int(carisma * 1.3)

        print("=============================")
        print("         PERSONAGEM          ")
        print("=============================")
        print(f'NOME: {nome}')
        print(f'RAÇA: {raca}')
        print(f'CLASSE: {classe}')
        print(f'MOEDAS: {moedas}')
        print(f'CAPACIDADE: {capacidade}Kg')
        print("=============================")
        print("          ATRIBUTOS          ")
        print("=============================")
        print(f'VIG: {vigor}')
        print(f'FOR: {forca}')
        print(f'DEF: {defesa}')
        print(f'INT: {intelecto}')
        print(f'PIE: {piedade}')
        print(f'DES: {destreza}')
        print(f'CAR: {carisma}')
        print("=============================")
        print("         INVENTÁRIO          ")
        print("=============================")
        itens.ExibirItem()
        print("=============================")
        print("           AÇÕES             ")
        print("=============================")
        print("1. Avançar Masmorra")
        acoes = input()

        if acoes == "1":
            os.system('clear')
            eventos.EscolherEventos()

    if raca1 == "2":
        raca = "Elfo"
        capacidade += 90
        forca = random.randrange(5,10)
        defesa = random.randrange(10,15)
        vigor = random.randrange(20,25)
        intelecto = random.randrange(20,25)
        piedade = random.randrange(15,20)
        destreza = random.randrange(15,20)
        carisma = random.randrange(5,10)

        intelecto = int(intelecto * 1.5)
        vigor = int(vigor * 1.3)
        
        print("=============================")
        print("         PERSONAGEM          ")
        print("=============================")
        print(f'NOME: {nome}')
        print(f'RAÇA: {raca}')
        print(f'CLASSE: {classe}')
        print(f'MOEDAS: {moedas}')
        print(f'CAPACIDADE: {capacidade}Kg')
        print("=============================")
        print("          ATRIBUTOS          ")
        print("=============================")
        print(f'VIG: {vigor}')
        print(f'FOR: {forca}')
        print(f'DEF: {defesa}')
        print(f'INT: {intelecto}')
        print(f'PIE: {piedade}')
        print(f'DES: {destreza}')
        print(f'CAR: {carisma}')
        print("=============================")
        print("         INVENTÁRIO          ")
        print("=============================")
        itens.ExibirItem()
    
    if raca1 == "3":
        raca = "Anão"
        capacidade += 210
        forca = random.randrange(20,25)
        defesa = random.randrange(20,25)
        vigor = random.randrange(15,20)
        intelecto = random.randrange(0,5)
        piedade = random.randrange(5,10)
        destreza = random.randrange(0,5)
        carisma = random.randrange(5,10)

        defesa = int(defesa * 1.5)
        forca = int(forca * 1.3)
        
        print("=============================")
        print("         PERSONAGEM          ")
        print("=============================")
        print(f'NOME: {nome}')
        print(f'RAÇA: {raca}')
        print(f'CLASSE: {classe}')
        print(f'MOEDAS: {moedas}')
        print(f'CAPACIDADE: {capacidade}Kg')
        print("=============================")
        print("          ATRIBUTOS          ")
        print("=============================")
        print(f'VIG: {vigor}')
        print(f'FOR: {forca}')
        print(f'DEF: {defesa}')
        print(f'INT: {intelecto}')
        print(f'PIE: {piedade}')
        print(f'DES: {destreza}')
        print(f'CAR: {carisma}')
        print("=============================")
        print("         INVENTÁRIO          ")
        print("=============================")
        itens.ExibirItem()
    
    if raca1 == "4":
        raca = "Gnomo"
        capacidade += 110
        forca = random.randrange(5,10)
        defesa = random.randrange(5,10)
        vigor = random.randrange(15,20)
        intelecto = random.randrange(20,25)
        piedade = random.randrange(20,25)
        destreza = random.randrange(15,20)
        carisma = random.randrange(10,15)

        piedade = int(piedade * 1.5)
        intelecto = int(intelecto * 1.3)
        
        print("=============================")
        print("         PERSONAGEM          ")
        print("=============================")
        print(f'NOME: {nome}')
        print(f'RAÇA: {raca}')
        print(f'CLASSE: {classe}')
        print(f'MOEDAS: {moedas}')
        print(f'CAPACIDADE: {capacidade}Kg')
        print("=============================")
        print("          ATRIBUTOS          ")
        print("=============================")
        print(f'VIG: {vigor}')
        print(f'FOR: {forca}')
        print(f'DEF: {defesa}')
        print(f'INT: {intelecto}')
        print(f'PIE: {piedade}')
        print(f'DES: {destreza}')
        print(f'CAR: {carisma}')
        print("=============================")
        print("         INVENTÁRIO          ")
        print("=============================")
        itens.ExibirItem()
        
