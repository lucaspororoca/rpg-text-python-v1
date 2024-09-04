import character

nome = ""
raca = 0
classe = 0

print("Qual seu nome?")
nome = input()
print("Qual sua Raça?")
raca = input()
print("Qual sua classe?")
classe = input()

character.CriarPersonagem(classe, raca)