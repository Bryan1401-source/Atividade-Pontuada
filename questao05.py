import os
from colorama import init, Fore

os.system("cls")

print(Fore.WHITE + """
    
    ================ $$$ Operações $$$ =================
         Multiplicação (*)
         Divisão (/)
         Subtração (-)
         Adição (+)
      
      """)

valor_A = int(input("Digite o valor do A: "))
valor_B = int(input("Digite o valor do B: "))
operacao = input("Digite um caractere")

match operacao:
    case "*":
        resultado = (valor_A * valor_B)
        print ("É uma multiplicação")
    case "/":
        resultado = (valor_A / valor_B)
        print ("É uma divisao")
    case "-":
        resultado = (valor_A - valor_B)
        print ("É uma subtração")
    case "+":
        resultado = (valor_A + valor_B)
        print ("É uma adição")
    case _:
        print ("\n A Operação não existe")
        resultado = 0
        
        
print (f"Resultado: ", resultado)