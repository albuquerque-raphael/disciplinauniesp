num1 = [int(input('Digite um numero inteiro: ')) for x in range(2)]
num_real = float(input("Digite um número real: "))

print(f"O produto do dobro do primeiro com metade do segundo é {(num1[0] * 2) * (num1[1] / 2)}")

print(f"A soma do triplo do primeiro com o terceiro é: {3 * num1[0] + num_real}")

print(f"O terceiro elevado ao cubo é {num_real ** 3:.2f}")