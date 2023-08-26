num = int(input("Digite um número para verificarmos se é primo ou não: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("O numero {} é DIVISÍVEL por {}".format(c, num))
        tot += 1
    else:
        print("O número {} não é divisível por {}".format(c, num))
print("O número {} foi divisível {} vezes".format(num, tot))
if tot == 2:
    print("Por isso, ele é um número PRIMO")
else:
    print("Por isso, ele não é primo") 
    