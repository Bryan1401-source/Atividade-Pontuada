import os
from colorama import init, Fore

os.system("cls")

print(Fore.WHITE + """
    ---------- $$$ Até 5 KG $$$ ---- | ------ $$$ Acima de 5 KG $$$ ------ 
    Morango |    R$ 2,50 por KG      |           R$ 2,20 por KG
     Maçã   |    R$ 1,80 por KG      |           R$ 1,50 por KG
""")

qtd_morango = float(input("Digite a quantidade de morango (KG): "))
qtd_maca = float(input("Digite a quantidade de maçã (KG): "))


if qtd_morango <= 5:
    preco_morango = qtd_morango * 2.50
else:
    preco_morango = qtd_morango * 2.20


if qtd_maca <= 5:
    preco_maca = qtd_maca * 1.80
else:
    preco_maca = qtd_maca * 1.50

# Totais
total_peso = qtd_morango + qtd_maca
total_pagar = preco_morango + preco_maca


if total_peso > 8 or total_pagar > 15.00:
    desconto = total_pagar * 0.10
    total_pagar -= desconto
else:
    desconto = 0

print(f"\nQuantidade de Morangos: {qtd_morango} KG")
print(f"Quantidade de Maçãs: {qtd_maca} KG")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"{Fore.GREEN}Valor Final a Pagar: R$ {total_pagar:.2f}")
