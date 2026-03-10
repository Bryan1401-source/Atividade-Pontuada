import os
from colorama import init, Fore

os.system("cls")

print(Fore.WHITE + """
    
    ================ $$$ Média Escolar $$$ =================
    Aprovado             Recuperação           Reprovado
    
    
                                        15:46   |   10/03/2026
    
    
    """)
      
primeira_nota = float(input("Digite a sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media >= 6.0:
    print ("Você está aprovado")
elif media == 4:
    print ("Você está na recuperação")
elif media < 4:
    print("Você está reprovado")
    
print ("\n Primeira Nota", primeira_nota)
print ("\n Segunda Nota", segunda_nota)
print ("\n Media", media)