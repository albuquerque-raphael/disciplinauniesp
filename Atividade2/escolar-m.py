nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Notas: {nota1} e {nota2}")
print("Média: ", media)
print("Conceito: ", conceito)

if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")