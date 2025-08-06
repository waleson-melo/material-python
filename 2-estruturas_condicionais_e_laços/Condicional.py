# idade = int (input("Digite sua idade: "))
# if idade < 18:
#     print("Você é menor de idade.")
# elif idade < 60:
#     print("Você é maior de idade.")
# else:
#     print("Você é idoso.")


# while idade < 18:
#     print("Você é menor de idade.")
#     idade = int(input("Digite sua idade novamente: "))


# for i in range(5):
#     print("Valor de i:", i)


# for i in range(1, 10, 2):
#     print("Valor de i:", i)

# while True:
#     comando = input("Digite 'sair' para parar")
#     if comando == "sair":
#         break

# for i in range(1, 10):
#     if i % 2 != 0:
#         continue
#     print("Valor de i:", i)   


# for i in range(3):
#     pass # print("Este código ainda não foi implementado.")

# while True:
#     numero = int(input("Digite um número: "))
#     if numero < 0:
#         print("Número negativo.")
#     elif numero == 0:
#         print("Número é zero.")
#     else:
#         print("Número positivo.")
#     if numero == 999:
#         print("Saindo do loop.")
#         break
#     print("Você digitou:", numero)

# contador = 1
# while contador <= 10:
#     print("Contador:", contador)
#     contador += 1

# while True:
#     numero = input("Digite um número para ver a tabuada (ou 'sair' para encerrar): ")
#     if numero.lower() == "sair":
#         print("Encerrando o programa.")
#         break
#     if numero.isdigit():
#         numero = int(numero)
#         for i in range(1, 11):
#             print(f"{numero} x {i} = {numero * i}")
#     else:
#         print("Entrada inválida. Por favor, digite um número ou 'sair'.")

numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")