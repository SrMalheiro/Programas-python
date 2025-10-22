#Importar
import string

#Variaveis
Numeros = []
SomaNumeros = 0
Quantidade = 0
MaiorNumero = 0

Palavras = []
MaiorPalavra = []

#Menu base
print("------------------------------------------")
print("Olá, seja bem vindo ao desafio interações!")
print("------------------------------------------")
print("")

#Perguntas e Funções
while True:
    num = int(input("Escreva números para uma sequência, um de cada vez! Use 0 para acabar a sequência: "))

    if num>MaiorNumero:
        MaiorNumero = num

    if num != 0:
        Quantidade = Quantidade+1

    SomaNumeros = SomaNumeros+num

    
    if num == 0:
        break
    
    Numeros.append(num)

Media = SomaNumeros/Quantidade

while True:
    pal = input("Escreva palavras para uma sequência, um de cada vez! Use 'fim' para acabar a sequência: ")

    QuantidadeLetras = len(pal)

    if QuantidadeLetras>4:
        MaiorPalavra.append(pal)
    
    if pal == 'fim':
        break
    
    Palavras.append(pal)

#Resposta
print("Sequência final de números:", Numeros)
print("Soma números:", SomaNumeros)
print("Média dos números:", Media)
print("Maior valor da sequência de números:", MaiorNumero)

print("Sequência final de palavras:", Palavras)
print("Palavras com pelo menos 5 caracteres:", MaiorPalavra)

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")