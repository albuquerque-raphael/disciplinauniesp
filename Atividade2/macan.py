quantidade_maca = int(input('Quantas maçãs deseja comprar: '))
if quantidade_maca >= 12:
    print(f'{quantidade_maca} maçãs custam R${quantidade_maca * 1.00:.2f}')
else:
    print(f'{quantidade_maca} maçãs custam R${quantidade_maca * 1.30:.2f}')  