#Variáveis
AlfabetoMaiusculas = "abcdefghijklmnopqrstuvwxyz"
AlfabetoMinusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Funcoes
def PerguntasIniciais():
    texto = input("Insira o texto que quer 'cifrar': ")
    while True:
        chave = input("Que tipo de chave quer usar para 'cifrar'? ")
        if chave.lstrip('-').isdigit():
            break
        else:
            print("ERRO | Resposta inválida... Insira novamente...")
            print()
    
    intchave = int(chave)
    return texto, intchave

def Cifra(alfabetoMAIUSCULAS, alfabetoMINUSCULAS, texto, chave):
    resultado = ""
    for letra in texto:
        if letra in alfabetoMAIUSCULAS:
            posicao = alfabetoMAIUSCULAS.index(letra)
            nova_posicao = (posicao + chave) % 26
            resultado += alfabetoMAIUSCULAS[nova_posicao]

        elif letra in alfabetoMINUSCULAS:
            posicao = alfabetoMINUSCULAS.index(letra)
            nova_posicao = (posicao + chave) % 26
            resultado += alfabetoMINUSCULAS[nova_posicao]

        else:
            # Mantém espaços, pontuação, números, etc.
            resultado += letra
    
    return resultado

#Menu base
print("-------------------------------------------------")
print("Olá, seja bem vindo ao desafio de cifra de césar!")
print("-------------------------------------------------")
print("")

#Programa
Texto, Chave = PerguntasIniciais()
Resultado = Cifra(AlfabetoMaiusculas, AlfabetoMinusculas, Texto, Chave)
print("O resultado foi: " + Resultado)

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")