import moeda
print('Desafio 030 - Funções para aumentar e diminuir valores')
valor = float(input('Digite o valor: R$ '))
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(valor, 13))}')
if valor == 0:
    print('Preço inválido tente novamente!')
    
