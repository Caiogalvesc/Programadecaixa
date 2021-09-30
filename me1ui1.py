S = 'S'
N = 'N'
fim = ''
codigo = media = maior = qtdhomem = 0
nomef = ''
while fim != S:
    print(11 * '-=')
    print('MINI MERCADO BARATINHO')
    print(11 * '-=', '\n')

    codigo = codigo + 1
    print('***O código desse cliente é: 00{}'.format(codigo))
    nome = input('Insira o nome do cliente: ')
    sexo = input('Qual o sexo do cliente? (Digite M-masculino ou F-feminino) \n')

    print(39 * '-=')
    print('Digite 0, tanto no valor, como na quantidade, quando não houver mais produtos.')
    print(39 * '-=', '\n')

    produto = float(input('Insira qual o valor do 1º produto: R$'))
    qte = int(input('Informe a quantidade desejada: \n'))
    valortotal = 0

    while produto and qte != 0:
        valortotal = valortotal + (produto * qte)
        produto = float(input('Insira qual o valor do próximo produto: R$ '))
        qte = int(input('Informe a quantidade desejada. \n'))
        media = media + valortotal
    if valortotal > maior and sexo == 'F':
        maior = valortotal
        nomef = nome
    if sexo == 'M':
        qtdhomem = qtdhomem + 1

    print('***O preço total foi de: R${:.2f}***\n'.format(valortotal))
    fim = input('O dia foi encerrado? (Digite S = Sim / N = Não)\n ')

if fim == S:
    print('***{} clientes fizeram compras hoje.***\n'.format(codigo))
    print('***R${:.2f} é a média da soma de todos os valores de compra realizadas hoje.***\n'.format(media/codigo))
    print('***A mulher com maior valor de compra foi {} e ela comprou R${}***\n'.format(nomef, maior))
    print('***{}% dos clientes de hoje foram homens.***'.format(qtdhomem * 100 / codigo))
