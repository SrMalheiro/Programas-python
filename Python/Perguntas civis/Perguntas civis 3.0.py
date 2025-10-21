import string

#Variaveis
Opcao=0

#Perguntas
while Opcao!=1:
    #Menu Inicial
    print("-----------------------")
    print("Bem vindo ao inquérito!")
    print("-----------------------")
    print()

    Nome = input("Insira o seu nome: ")

    Idade = input("Insira a sua data de nascimento (Formato: xx/yy/zzzz): ")

    Nif = int(input("Insira o seu NIF (Número de Identificação Físcal): "))
    CountNif = len(str(Nif))
    while CountNif!=9:
        Nif = int(input("ERRO: NIF INVÁLIDO! | Insira o NIF novamente: "))
        CountNif = len(str(Nif))

    Profissao = input("Insira a sua profissão: ")

    NivelEscolaridade = input("Insira o seu nível de escolaridade: ")

    Cidade = input("Insira a cidade aonde reside ou irá residir brevemente: ")

    Concelho = input("Insira o concelho aonde reside ou irá residir brevemente: ")

    Rua = input("Insira a rua aonde reside ou irá residir brevemente: ")

    Cp = input("Insira o código postal aonde reside ou irá residir brevemente: ")
    
    print("À seguinte pergunta, responde em texto corrido!")
    Ingressar = input("Insere o que gostavas de fazer: ")

    #Imprimir relatório
    nome_ficheiro = f"{Nome}.txt"

    with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
        ficheiro.write(f"Nome: {Nome}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"Idade: {Idade}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"NIF: {Nif}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"Profissão: {Profissao}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"Nivel de Escolaridade: {NivelEscolaridade}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"Morada: {Cidade}, {Concelho}, {Rua}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"Código Postal: {Cp}\n")
        ficheiro.write(f"\n")
        ficheiro.write(f"Estilo de emprego desejado: {Ingressar}\n")

    #FIM
    print()
    print()
    print("O seu questionário foi salvo, aguarde 15 a 20 dias pelo EMail do centro de emprego!")
    print()
    print("Questionário Finalizado...")
    print()
    print("Para outra pessoa fazer o questionário escreva 2 e 'ENTER'")
    print("Para fechar o questionário escreva 1 e 'ENTER'")
    Opcao = int(input("Resposta:"))
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()