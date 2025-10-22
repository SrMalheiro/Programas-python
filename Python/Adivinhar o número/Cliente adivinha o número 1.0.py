#Importar
import random

#Variaveis
tentativa = -1
numeroTentativas = 0

#Menu
print("--------------------------------------------------")
print("Olá, seja bem vindo ao jogo de adivinhar o número!")
print("--------------------------------------------------")
print("")

#Escolha de quantidade de números variáveis
quantidadeVariaves = int(input("Insira o máximo de números que quer para a adivinha, de 0 ao número que escolheres: "))

#O computador gere um número aleatório
numeroAleatorio = random.randint(0, quantidadeVariaves)

#Adivinha
while (tentativa!=numeroAleatorio):
    numeroTentativas=numeroTentativas+1
    tentativa = int(input("Insere a tua adivinha: "))
    while (tentativa<0 or tentativa>quantidadeVariaves):
        print("")
        print("Deves inserir um valor entre 0 e", quantidadeVariaves, ", com ambos os números inclusos na adivinha!")
        tentativa = int(input("Insere um número viável: "))
        numeroTentativas=numeroTentativas+1

    if (tentativa>numeroAleatorio):
        print("Tenta novamente, mas um número menor desta vez!")
    
    if (tentativa<numeroAleatorio):
        print("Tenta novamente, mas um número maior desta vez!")
    
    if (tentativa==numeroAleatorio):
        print("ACERTASTE,", numeroAleatorio, "era o número correto!")
        print("Acertaste em", numeroTentativas, "tentativas!")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")
    