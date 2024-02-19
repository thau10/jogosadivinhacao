print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 16

chuteString = input('Digite um número: ')

print('Você digitou o número: ', chuteString)

chute = int (chuteString)

if numeroSecreto == chute:
    print('Você acertou!')

else:
    print('Você errou!')

