from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções: 
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] Tesoura""")
jogador = int(input("Qual é a sua jogada? "))
print("-=" * 10)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {} ".format(itens[jogador]))
print("-=" * 10)