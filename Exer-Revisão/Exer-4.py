print("-=" * 20)
print("LEIA UMA LISTA DE NÚMEROS E DIGA MAIOR E MENOR")
print("-=" *20)

resp = "S"
quant = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
print("O maior valor foi {} e o menor valor foi {}".format(maior, menor))

