#Importar
import string

#Variaveis
DadosUtilizador = "Malheiro"
DadosSenha = "python123"

#Menu base
print("------------------------------------------------")
print("Olá, seja bem vindo ao desafio utilizador/senha!")
print("------------------------------------------------")
print("")

#Perguntas
Utilizador = input("Insere o utilizador: ")
while Utilizador != DadosUtilizador:
    Utilizador = input("UTILIZADOR ADMINISTRADOR ERRADO! | Insere o utilizador: ")

Senha = input("Insere a palavra-pass: ")
while Senha != DadosSenha:
    Senha = input("UTILIZADOR ADMINISTRADOR ERRADO! | Insere o utilizador: ")

#Só para deixar mais bonito
print()
print("DADOS INSERIDOS CORRETAMENTE!")

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")