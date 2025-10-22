#Importar
import random
import os

#Variaveis
Dicionario = []
Temas = ["animais", "cinema", "comida", "desporto", "paises", "tecnologia"]

#Funcoes
def carregar_palavras(nome):
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, nome)
    with open(caminho, encoding="utf-8") as f:
        dicionario = [linha.strip() for linha in f.readlines()]
    return dicionario

def EscolherTema(temas):
    print(f"Os temas dísponiveis são: {temas}")
    while True:
        temanormal = input("Qual tema escolhe? ")
        tema = temanormal.lower()
        
        if tema.isdigit():
            print("ERRO | Não pode escrever números!")
        
        elif tema not in temas:
            print("Tema indísponivel")

        else:
            break
    
    return tema

#Menu base
print("-------------------------------------")
print("Olá, seja bem vindo ao jogo da forca!")
print("-------------------------------------")
print("")

#Programa
DicionarioAnimais = carregar_palavras("animais.txt")
DicionarioCinema = carregar_palavras("cinema.txt")
DicionarioComida = carregar_palavras("comida.txt")
DicionarioDesporto = carregar_palavras("desporto.txt")
DicionarioPaises = carregar_palavras("paises.txt")
DicionarioTecnologia = carregar_palavras("tecnologia.txt")

Tema = EscolherTema(Temas)

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")