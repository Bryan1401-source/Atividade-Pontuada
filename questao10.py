import os
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

print(Fore.WHITE +""")
      
   ========|
   Alcool  | Até 25L, desconto de 2% por litro | Acima de 25L, desconto de 3% por litro
   ========|
   Gasolina| Até 25L, desconto de 3% por litro | Acima de 25L, desconto de 5% por litro
   ========|   
      
      
      """)

litros = float(input("Digite o número de litros: "))
tipo = input("Digite o tipo (A-álcool, G-gasolina): ").upper()

if tipo == 'A':
    preco_base = 3.79
  
    desconto = 0.02 if litros <= 25 else 0.03
elif tipo == 'G':
    preco_base = 6.59
  
    desconto = 0.03 if litros <= 25 else 0.05
else:
    print("Tipo inválido!")
    exit()

valor_total = (litros * preco_base) * (1 - desconto)
print(f"Valor a pagar: R$ {valor_total:.2f}")
   