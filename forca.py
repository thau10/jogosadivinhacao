def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    #Definir qual a palavra secreta
    palavraSecreta = "banana"

    enforcou = False
    acertou = False

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        print("Jogando....")
        chute = input("Qual a letra?")
        index = 0
        for letra in palavraSecreta:
            if(chute ==letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1
            

            print("jogando...")    


    print("Fim de jogo!")
if(__name__ == "__main__"):
    jogar_forca()