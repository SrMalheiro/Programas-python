#Importar
import random

#Variaveis
caracteres = "1234567890abcdefghijklmnopqrstuvwxyz!@#ç"

#Menu
print("-----------------------------------------------")
print("Olá, seja bem vindo ao gerador de palavra-pass!")
print("-----------------------------------------------")
print("")

#Area Cliente
quantidadeCaracteres = int(input("De quantos caracteres vai ser a password? "))

#Programa
for i in range(0, quantidadeCaracteres):
    caracterRandom = random.choice(caracteres)
    print(caracterRandom, end="")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")
