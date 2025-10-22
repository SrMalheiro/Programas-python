#Importar
import string

#Menu base
print("-------------------------------------------------")
print("Olá, seja bem vindo à minha primeira calculadora!")
print("-------------------------------------------------")
print("")

#Escolha de qual cálculo fazer
print("Na seguinte pergunta use as informações seguintes:")
print("Para SOMAR use '+'")
print("Para SUBTRAIR use '-'")
print("Para MULTIPLICAR use '*'")
print("Para DIVIDIR use '/'")
opcao = input("Que tipo de cálculo quer realizar? ")

#Quais os valores
num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o segundo valor: "))

#Função
if(opcao=='+'):
    resultado = num1+num2
    print("A soma dos dois números é:", str(resultado))
    
if(opcao=='-'):
    resultado = num1-num2
    print("A subtração dos dois números é:", str(resultado))

    
if(opcao=='*'):
    resultado = num1*num2
    print("A multiplicação dos dois números é:", str(resultado))

    
if(opcao=='/'):
    resultado = num1/num2
    print("A divisão dos dois números é:", str(resultado))

#FIM
print("")
print("Programa finalizado.")
input("Pressione Enter para encerrar...")