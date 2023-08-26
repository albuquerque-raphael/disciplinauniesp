print("-=" * 14)
print("VERIFICAR SE É PAR OU ÍMPAR!")
print("-=" *14)

n = int(input("Digite número qualquer: "))
resultado = n % 2
print("O resultado foi {}".format(resultado))
if resultado == 0:
    print("Então o número é PAR")
else:
    print("Então o número é ÍMPAR")
