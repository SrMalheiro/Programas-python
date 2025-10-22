#Importar
import string

#Variáveis
ApareceA = "A", "À", "Á", "Â", "Ã", "a", "à", "á", "â", "ã"
ApareceE = "E", "É", "È", "Ê", "e", "é", "è", "ê"
ApareceI = "I", "Í", "Ì", "Î", "i", "í", "ì", "î"
ApareceO = "O", "Ó", "Ò", "Ô", "Õ", "o", "ó", "ò", "ô", "õ"
ApareceU = "U", "Ú", "Ù", "Û", "u", "ú", "ù", "û"

QuantidadeA = 0
QuantidadeE = 0
QuantidadeI = 0
QuantidadeO = 0
QuantidadeU = 0

#Menu base
print("-----------------------------------------------------")
print("Olá, seja bem vindo ao desafio de contador de vogais!")
print("-----------------------------------------------------")
print("")

#Perguntas
Texto = input("Escreva um texto ou palavra que irei contar a quantidade de vogais: ")

#Função
for letra in Texto:
    if letra in ApareceA:
        QuantidadeA +=1
    if letra in ApareceE:
        QuantidadeE +=1
    if letra in ApareceI:
        QuantidadeI +=1
    if letra in ApareceO:
        QuantidadeO +=1
    if letra in ApareceU:
        QuantidadeU +=1

QuantidadeTotal = QuantidadeA + QuantidadeE + QuantidadeI + QuantidadeO + QuantidadeU

#Resposta
print("Quantidade da vogal A:" + str(QuantidadeA))
print("Quantidade da vogal E:" + str(QuantidadeE))
print("Quantidade da vogal I:" + str(QuantidadeI))
print("Quantidade da vogal O:" + str(QuantidadeO))
print("Quantidade da vogal U:" + str(QuantidadeU))
print()
print("Quantidade final de vogais:" + str(QuantidadeTotal))

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")