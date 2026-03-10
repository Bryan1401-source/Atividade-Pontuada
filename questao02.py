import os

from colorama import init, Fore, Back, Style

# Limpe o terminal.
os.system("cls")

print (Fore.BLACK + """
       
       ------------- Digite os seus dados -----------
       """)
print(Style.RESET_ALL) 


nome = input(Fore.BLACK + "Digite seu nome: ")
sexo = input(Fore.BLACK +"Digite seu gênero: ")
estado_civil = input(Fore.BLACK + "Digite seu estado cívil: ")

if sexo == "F" and estado_civil == "CASADA":
   print(input("Digite seu tempo de Relacionamento: "))






