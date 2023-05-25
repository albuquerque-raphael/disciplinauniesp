estoque_atual = int(input("Digite a quantidade atual em estoque: "))
estoque_maximo = int(input("Digite a quantidade máxima em estoque: "))
estoque_minimo = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (estoque_maximo + estoque_minimo) / 2

print("A quantidade média em estoque é:", quantidade_media)

if estoque_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")