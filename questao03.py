import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print (Fore.YELLOW + """
       
       ------------- Digite os Valores -----------
       """)

valorA = int(input("Digite um valor pro A: "))
valorB = int(input("Digite um valor pro B: "))

if valorA == valorB:
    resultado = (valorA + valorB)
    
else:  resultado = (valorA*valorB)


print ("\n Valor A:", valorA)
print (" Valor B:", valorB)
print (" Valor C:",resultado)

print(Style.RESET_ALL) 