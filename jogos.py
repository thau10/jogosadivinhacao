import forca;
import jogoadivinhacao;
print("*************")
print("*********** Escolha seu jogo!********")
print("*********************")

print("(1) Forca (2) Adivinhacão")

jogo = int(input ( "Qual jogo?"))

#Criando a condição
if(jogo ==1):
    print("jogando jogo Forca")
    forca.jogar_forca()
else:
    print( "Jogando o jogo da adivinhação")
    Jogoadivinhacao.jogar_adivinhacao()

