import os
from colorama import init, Fore

os.system("cls")

print(Fore.WHITE + """
      
 ------------- $$$ Loja de CD $$$ -------------- 
    Cor                             Preço
    Verde                           R$ 10,00
    Azul                            R$ 20,00
    Amarelo                         R$ 30,00
    Vermelho                        R$ 40,00
    
      """)

cor = input("Digite o nome de uma cor: ")

match cor:
    case "Verde":
        print("R$ 10,00")
    case "Azul":
        print("R$ 20,00")
    case "Amarelo":
        print ("R$ 30,00")
    case "Vermelho":
        print ("R$ 40,00")
    case _:
        print ("Tinta não encontrada.")

