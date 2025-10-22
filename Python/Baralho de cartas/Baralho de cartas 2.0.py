#----------Importar----------
import random

#----------Funções----------
def perguntas_iniciais():
    while True:
        QuantosBaralhos = int(input("Quantos baralhos vai usar? "))
        if QuantosBaralhos > 0:
            break
        else:
            print("Erro: o número de baralhos deve ser maior que 0.\n")
    
    while True:
        QuantosJogadores = int(input("Quantos jogadores são? "))
        if QuantosJogadores > 0:
            break
        else:
            print("Erro: o número de jogadores deve ser maior que 0.\n")
    
    while True:
        QuantasCartas = int(input("Quantas cartas por cada jogador são? "))
        if QuantasCartas > 0:
            break
        else:
            print("Erro: o número de cartas deve ser maior que 0.\n")
    
    TotalCartas = 52
    
    while True:
        ComSemCuringa = input("Quer adicionar Curingas? (sim ou não) ")
        if (ComSemCuringa == "sim" or ComSemCuringa == "Sim"):
            ComSemCuringa = True
            TotalCartas += 2
            break
        elif (ComSemCuringa == "não" or ComSemCuringa == "nao" or ComSemCuringa == "Não" or ComSemCuringa == "Nao"):
            ComSemCuringa = False
            break
        else:
            print("Resposta inválida...")
            print()
    while True:
        Embaralhar = input("Quer embaralhar as cartas? (sim ou não) ")
        if (Embaralhar == "sim" or Embaralhar == "Sim"):
            Embaralhar = True
            break
        elif (Embaralhar == "não" or Embaralhar == "nao" or Embaralhar == "Não" or Embaralhar == "Nao"):
            Embaralhar = False
            break
        else:
            print("Resposta inválida...")
            print()

    TotalCartas = TotalCartas*QuantosBaralhos

    return QuantosBaralhos, ComSemCuringa, Embaralhar, TotalCartas, QuantosJogadores, QuantasCartas

def gerar_baralho(QuantosBaralhos, ComSemCuringa, Embaralhar):
    cartas_sem_curinga = {
        "♠": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        "♣": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        "♥": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        "♦": ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
    }
    cartas_curinga = ["🃏 Vermelho", "🃏 Preto"]

    Baralho = []
    for i in range(QuantosBaralhos):
        for naipe, valores in cartas_sem_curinga.items():
            for valor in valores:
                Baralho.append(f"{valor}{naipe}")
        
        if ComSemCuringa:
            Baralho.extend(cartas_curinga)
    
    if Embaralhar:
        random.shuffle(Baralho)

    return Baralho

def mostrar_baralho(Baralho):
    print(f"O baralho tem {len(Baralho)} cartas:")
    print(", ".join(Baralho))

def dar_as_cartas(Baralho, QuantosJogadores, QuantasCartas):
    if QuantosJogadores * QuantasCartas > len(Baralho):
        print("Erro: não há cartas suficientes!")
        return [], Baralho

    Jogadores = []
    for i in range(QuantosJogadores):
        Mao = []
        for j in range(QuantasCartas):
            Mao.append(Baralho.pop(0))
        Jogadores.append(Mao)

    return Jogadores, Baralho

def mostrar_jogadores(Jogadores):
    for i, Mao in enumerate(Jogadores, start=1):
        print(f"Jogador {i} ({len(Mao)} cartas): {', '.join(Mao)}")


#----------Menu Base----------
print("-----------------------------------------------------")
print("Olá, seja bem vindo ao programa de baralho de cartas!")
print("-----------------------------------------------------")
print("")

#----------Perguntas----------
Quantos_baralhos, Com_sem_curinga, Embaralhar, Total_cartas, Quantos_jogadores, Quantas_cartas  = perguntas_iniciais()

#----------Programa----------
Baralho = gerar_baralho(Quantos_baralhos, Com_sem_curinga, Embaralhar)
mostrar_baralho(Baralho)
Jogadores, Baralho = dar_as_cartas(Baralho, Quantos_jogadores, Quantas_cartas)
mostrar_jogadores(Jogadores)
print()
print("Baralho restante:")
mostrar_baralho(Baralho)

#----------FIM----------
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")