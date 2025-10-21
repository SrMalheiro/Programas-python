#Importar
import random

#Variaveis
OpcoesDados = [1, 2, 3, 4, 5, 6]

#Funcoes
def QuantosDados():
    quantidadeLetra = input("Quantidade de dados a ser jogados: ")
    while True:
        if quantidadeLetra.isdigit():
            break
        else:
            print("ERRO | A quantidade tem de ser um número!")
            print()
            quantidadeLetra = input("Insira novamente... quantidade de dados a ser jogados: ")
    
    quantidade = int(quantidadeLetra)
    return quantidade

def EscolherDados(quantidade, opcoes):
    resultados = random.choices(opcoes, k=quantidade)
    return resultados

def Respostas(resultados):
    print(f"O resultado dos dados foi: {resultados}")

#Menu base
print("------------------------------------------------")
print("Olá, seja bem vindo ao jogo de dados aleatórios!")
print("------------------------------------------------")
print("")

#Programa
while True:
    print()
    Acao1 = input("Para repetir ou começar clique 'enter', para sair escreva qualquer coisa e presssione 'enter': ")
    if Acao1=="":
        Quantidade = QuantosDados()
        Resultados = EscolherDados(Quantidade, OpcoesDados)
        #Resposta
        Respostas(Resultados)
    else:
        break

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")