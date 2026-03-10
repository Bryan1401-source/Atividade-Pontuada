import os
from colorama import init, Fore

os.system("cls")

print(Fore.WHITE + """
      
      =============== $$$ Produtos $$$ =================
  
                                            10/03/2026
      """)

nome = input("Digite a descrição do Produto: ")
preco = float(input("Digite o preço do Produto: "))
quantidade = int(input("Digite a quantidade do seu Produto: "))

total = (quantidade * preco)

if quantidade <= 5:
    desconto = total * 0.02
elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
elif quantidade > 10:
    desconto = total * 0.10
else:
    desconto = 0
    
print(f"\n Nome do Produto: {nome}")
print(f"Preço: {preco} reais")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"{Fore.GREEN}Valor Total a Pagar: R$ {total:.2f}")