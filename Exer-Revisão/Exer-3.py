print("-=" * 18)
print("ESCREVER UM NÚMERO PAR DO 0 ATÉ ELE!")
print("-=" *18)

n = 0
n = int(input("Digite número PAR: "))
n = n + 1
for n in range(0, n):
    if n % 2 == 0:
        print(n)
        