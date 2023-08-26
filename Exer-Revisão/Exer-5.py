soma = 0
cont = 0
media = 0
for c in range(1, 7):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma += num 
        cont += 1
        media = soma / cont
print("Você informou {} números PARES e a soma foi {}".format(cont, soma))
print("A média dos números pares foi de {:.2f}".format(media))
