#Importar
import random

#Variaveis
acertoErro = -1
numeroTentativas = 0
texto = "A minha suposição é: "
Limite = 100
BaixoLimite = 0

#Menu
print("-------------------------------------------------------------")
print("Olá, seja bem vindo ao jogo do computador adivinhar o número!")
print("-------------------------------------------------------------")
print("")

#Escolha de quantidade de números variáveis
print("Pensa um número inteiro entre 0 e 100, não escrevas")
nothing = str(input("Pressiona 'enter' após pensares num número!"))

#Adivinha
while (acertoErro!=1):
    numeroTentativas=numeroTentativas+1

    numeroAdivinha = random.randint(BaixoLimite, Limite)
    print(texto, numeroAdivinha)
    acertoErro = int(input("Acertei? (1- Sim, 2- Maior, 3- Menor) "))
    if (acertoErro==2):
        BaixoLimite=numeroAdivinha
    
    if (acertoErro==3):
        Limite=numeroAdivinha
    
    if (acertoErro==1):
        print("YUPIII, acerteiiiiiii")
        print("Acertei em", numeroTentativas, "tentativas!")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")
    