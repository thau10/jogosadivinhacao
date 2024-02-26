print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

numeroSecreto = 16

chuteString = input('Digite um número: ')

print('Você digitou o número: ', chuteString)

chute = int (chuteString)

if numeroSecreto == chute:
    print('Você acertou!')
elif(chute>numeroSecreto):
        print('Voce errou!! O número secreto é numero menor')


else:
    print('Você errou!! O numero secreto é um número maior')

