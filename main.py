import character
import os

nome = ""
classe = 0
raca = 0

def Main():
    global nome
    global raca 
    global classe

    os.system('clear')    
    print("Qual seu nome?")
    nome = input()
    os.system('clear')

    print("Qual sua Raça?")
    print("1. Humano")
    print("2. Elfo")
    print("3. Anão")
    print("4. Gnomo")
    raca = input()
    os.system('clear')

    print("Qual sua classe?")
    print("1. Guerreiro")
    print("2. Mago")
    classe = input()
    os.system('clear')

    character.CriarPersonagem(nome, classe, raca)

Main()