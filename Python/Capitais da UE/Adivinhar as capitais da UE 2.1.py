#Importar
import time
import random
import csv
import os

#Variaveis
PaisesDisponiveis = {
    "Alemanha": ["Berlim", "Berlin", "berlim", "berlin"],
    "Áustria": ["Viena", "Vienna", "viena", "vienna"],
    "Bélgica": ["Bruxelas", "Brussels", "bruxelas", "brussels"],
    "Bulgária": ["Sófia", "Sofia", "sófia", "sofia"],
    "Chipre": ["Nicósia", "Nicosia", "nicósia", "nicosia"],
    "Croácia": ["Zagreb", "zagreb"],
    "Dinamarca": ["Copenhaga", "Copenhagen", "copenhaga", "copenhagen"],
    "Eslováquia": ["Bratislava", "bratislava"],
    "Eslovénia": ["Liubliana", "Ljubljana", "liubliana", "ljubljana"],
    "Espanha": ["Madrid", "madrid"],
    "Estónia": ["Tallinn", "tallinn"],
    "Finlândia": ["Helsínquia", "Helsinki", "helsínquia", "helsinquia", "helsinki"],
    "França": ["Paris", "paris"],
    "Grécia": ["Atenas", "Athens", "atenas", "athens"],
    "Hungria": ["Budapeste", "Budapest", "budapeste", "budapest"],
    "Irlanda": ["Dublin", "dublin"],
    "Itália": ["Roma", "Rome", "roma", "rome"],
    "Letónia": ["Riga", "riga"],
    "Lituânia": ["Vilnius", "vilnius"],
    "Luxemburgo": ["Luxemburgo", "Luxembourg", "luxemburgo", "luxembourg"],
    "Malta": ["Valletta", "valletta"],
    "Países Baixos": ["Amesterdão", "Amsterdam", "amesterdão", "amsterdam"],
    "Polónia": ["Varsóvia", "Warsaw", "varsóvia", "varsovia", "warsaw"],
    "Portugal": ["Lisboa", "Lisbon", "lisboa", "lisbon"],
    "Roménia": ["Bucareste", "Bucharest", "bucareste", "bucharest"],
    "Suécia": ["Estocolmo", "Stockholm", "estocolmo", "stockholm"]
}
PaisesNaoPerguntados = list(PaisesDisponiveis.keys())

#Funções
def RespostasDoPrograma(pontuacao, perguntas_total, tempo_execucao):
    if perguntas_total == 0:
        percentagem = 0
    else:
        percentagem = int((pontuacao / perguntas_total) * 100)

    print()
    print("Tempo total de jogo: " + str(tempo_execucao) + " segundos.")
    print()
    print("Score: " + str(pontuacao) + " de " + str(perguntas_total) + ".")
    print()
    print("Percentagem: " + str(percentagem) + "%")
    print()
    return percentagem

def EscolherPais():
    PaisDaUE = random.choice(PaisesNaoPerguntados)
    return PaisDaUE

def RespostaDigito(Pais):
    print("Não podes inserir números! A pergunta vai ser feita de novo...")
    print()
    Resposta = input("Qual é a capital de " + Pais +  "? (Escreve 'sair' para terminar...) ")
    return Resposta

def NumeroPerguntas():
    QuantasPerguntas = int(input("Quantas perguntas quer fazer? (Valores entre 1 e 26): "))
    while QuantasPerguntas<=0 or QuantasPerguntas>26:
        print("Número Inválido de perguntas...")
        QuantasPerguntas = int(input("Quantas perguntas quer fazer? (Valores entre 1 e 26): "))
    return QuantasPerguntas

def Questionario(quantas_perguntas):
    pontuacao = 0
    perguntas_total = 0

    while PaisesNaoPerguntados and perguntas_total < quantas_perguntas:
        pais = EscolherPais()
        PaisesNaoPerguntados.remove(pais) 

        resposta = input(f"Qual é a capital de {pais}? (Escreve 'sair' para terminar...) ")
        while resposta.isdigit():
            resposta = RespostaDigito(pais)

        if resposta.lower() == "sair":
            break

        if resposta in PaisesDisponiveis[pais]:
            print("Resposta correta!")
            pontuacao += 1
        else:
            resposta = RespostaErrada(pais)
            if resposta.lower() == "sair":
                break
            if resposta in PaisesDisponiveis[pais]:
                pontuacao += 1

        perguntas_total += 1
        print()

    return pontuacao, perguntas_total

def RespostaErrada(pais):
    print("Resposta errada...")
    print("Tente novamente!")

    resposta = input(f"Qual é a capital de {pais}? (Escreve 'sair' para terminar...) ")
    while resposta.isdigit():
        print("Não podes inserir números! A pergunta vai ser feita de novo...")
        print()
        resposta = input(f"Qual é a capital de {pais}? (Escreve 'sair' para terminar...) ")

    if resposta.lower() == "sair":
        return "sair"

    if resposta in PaisesDisponiveis[pais]:
        print("Resposta correta!")
    else:
        print("Resposta errada...")

    return resposta

#Menu base
print("-------------------------------------------------------------")
print("Olá, seja bem vindo ao desafio de capitais da União Europeia!")
print("-------------------------------------------------------------")
print("")

Nome = input("Insira o seu nome: ")
while Nome.isdigit():
    Nome = input("Insira o seu nome: ")

print()
print("Vamos começar...")
print()
QuantasPerguntas = NumeroPerguntas()

TempoInicio = time.time()

Pontuacao, PerguntasTotal = Questionario(QuantasPerguntas)

TempoFim = time.time()
TempoDeExecucao = int(TempoFim - TempoInicio)

Percentagem = RespostasDoPrograma(Pontuacao, PerguntasTotal, TempoDeExecucao)

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, "dados.csv")
ficheiro_existe = os.path.isfile(caminho_arquivo)
with open(caminho_arquivo, mode="a", newline="", encoding="utf-8") as ficheiro:
    escritor = csv.writer(ficheiro)
    if not ficheiro_existe:
        escritor.writerow(["Nome", "Tempo de jogo", "Pontuação", "Total", "Percentagem"])
    
    escritor.writerow([Nome, TempoDeExecucao, Pontuacao, PerguntasTotal, Percentagem])

print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")