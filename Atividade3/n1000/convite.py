convidados = ['James Headfild', 'Bonno Vox', 'Ellon Musk', 'Papa Francisco', 'Warren buffet']


mensagem = "Olá, você está convidado para um day off na minha casa. Espero contar com sua presença!"
for convidado in convidados:
    print(f"Enviando convite para {convidado}...")
    print(mensagem)
    print()


desistencia = 'James Headfild'
print(f"{desistencia} não poderá comparecer ao jantar.")
convidados.remove(desistencia)


print(f"Adicionando novo convidado...")
novo_convidado = 'Bill Gates'
convidados.append(novo_convidado)


print("Enviando novos convites...")
for convidado in convidados:
    print(f"Enviando convite para {convidado}...")
    print(mensagem)
    print()