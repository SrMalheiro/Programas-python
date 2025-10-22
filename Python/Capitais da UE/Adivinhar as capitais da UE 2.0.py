#Importar
import string
import random

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
Pontuacao = 0
PaisesNaoPerguntados = list(PaisesDisponiveis.keys())

#Funções
def EscolherPais():
    PaisDaUE = random.choice(PaisesNaoPerguntados)
    return PaisDaUE

#Menu base
print("-------------------------------------------------------------")
print("Olá, seja bem vindo ao desafio de capitais da União Europeia!")
print("-------------------------------------------------------------")
print("")

#Perguntas

while PaisesNaoPerguntados:
    Pais = EscolherPais()
    PaisesNaoPerguntados.remove(Pais) 

    Resposta = input("Qual é a capital de " + Pais +  "? (Escreve 'sair' para terminar...) ")
    while Resposta.isdigit():
        print("Não podes inserir números! A pergunta vai ser feita de novo...")
        print()
        Resposta = input("Qual é a capital de " + Pais +  "? (Escreve 'sair' para terminar...) ")

    if Resposta == "sair" or Resposta == "Sair":
        break

    if Resposta in [capital for capital in PaisesDisponiveis[Pais]]:
        print("Resposta correta!")
        Pontuacao +=1

    else:
        print("Resposta errada...")

    print()

PercentagemPontuacao = int((Pontuacao/26)*100)

print("A tua pontuação é: " + str(Pontuacao) + " de 26")
print("Acertaste " + str(PercentagemPontuacao) + "% de todas as perguntas.")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")