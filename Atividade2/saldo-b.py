conta = int(input("Digite o número da conta do cliente: "))
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual = saldo - debito + credito

print("O saldo atual da conta é:", saldo_atual)

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")