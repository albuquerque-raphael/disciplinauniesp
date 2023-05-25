nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2º nota: "))
media = (nota1 + nota2) / 2
if (media) >= 6:
    print(f'Você foi aprovado com media {media}')
else:
    print(f'infelizmente você foi reprovado com média {media}')