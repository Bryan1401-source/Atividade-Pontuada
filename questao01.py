import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print (Fore.LIGHTMAGENTA_EX + """
       
       ------------- Digite os valores -----------
       """)

print(Style.RESET_ALL) 


A = int(input(Fore.MAGENTA + "\nDigite o valor A: "))
B = int(input("\nDigite o valor B: "))
C = int(input("\nDigite o valor C: "))

print(Style.RESET_ALL) 


print (Fore.LIGHTMAGENTA_EX + """
       
       ------------- Resultados dos valores escolhidos -----------
       """)



if A + B < C:
    print("A Soma de A e B é menor que C")
else:
    print("A Soma de A e B é maior que C")


print(Style.RESET_ALL) 

print (Fore.LIGHTMAGENTA_EX + """
       
       ------------- FIM DA OPERAÇÃO -----------
       """)

print(Style.RESET_ALL) 
