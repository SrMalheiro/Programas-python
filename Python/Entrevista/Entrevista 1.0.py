#Importar
import string

#Menu base
print("------------------------------------------------------")
print("Olá, seja bem vindo ao programa de desafio entrevista!")
print("------------------------------------------------------")
print("")

#Perguntas
Nome = input("Qual é o teu nome? ")
print("Olá, "+Nome+"!")
Idade = int(input("Que idade tens? "))

#Função
NumeroLetras = int(len(Nome))
IdadeMaisTarde = int(Idade+5)

#Resposta
print("O teu nome tem "+ str(NumeroLetras) +" letras!")
print("Daqui a 5 anos terás "+ str(IdadeMaisTarde) +" anos!")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")