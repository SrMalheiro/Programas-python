#Importar
import string

#Variaveis
lista1 = [19, 8, 22, 35, 60, 73, 8, 90]
lista2 = [7, 12, 19, 7, 33, 45, 19, 60]
repetidos1 = []
repetidos2 = []

#Menu base
print("-------------------------------------------------------------")
print("Olá, seja bem vindo ao Desafio Iteração com múltiplas listas!")
print("-------------------------------------------------------------")
print("")

#Função e resposta
print("A lista 1 é: " + str(lista1))
print("A lista 2 é: " + str(lista2))
print()

    #Repetidos
for numero1 in lista1:
    if lista1.count(numero1) > 1 and numero1 not in repetidos1:
        repetidos1.append(numero1)

for numero2 in lista2:
    if lista2.count(numero2) > 1 and numero2 not in repetidos2:
        repetidos2.append(numero2)


if repetidos1:
    print("Os valores repetidos são:", repetidos1)
else:
    print("A lista não tem valores repetidos.")

if repetidos2:
    print("Os valores repetidos são:", repetidos2)
else:
    print("A lista não tem valores repetidos.")

    #Espaco
print()

    #Intersecao
Intersecao = set(lista1).intersection(lista2)
if Intersecao:
    print("Existem valores comuns nas duas listas e são: " + str(Intersecao))
else:
    print("Não existem valores comuns entre as listas.")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")