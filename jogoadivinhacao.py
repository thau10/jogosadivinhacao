import random

print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#definindo o  numero secreto
numeroSecreto = random.randrange(1,101)
#print(numeroSecreto)


#Definindo o numero de tentativas
numerotentativas = 10
rodada=1

print(" Qual o nível de dificuldade?")
print("(1)-Facíl,(2)-médio,(3)-difícil")

nivel = int(input)("Defina o nível:")

while(rodada<= numerotentativas):
    print('tentativa',rodada, 'de',numerotentativas)


#Recebendo o chute do jogador
    chuteString = input('Digite um número: ')


    chute = int (chuteString)

#Declarando as condições
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Voce errou!! O número secreto é numero menor')
    else:
        print('Você errou!! O numero secreto é um número maior')
    
    #numerotentativas = numerotentativas - 1
    rodada = rodada + 1






