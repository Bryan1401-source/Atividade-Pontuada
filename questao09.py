import os
from colorama import init, Fore

init(autoreset=True)
os.system("cls")

print(Fore.WHITE + """
      =============== $$$ Renda Mensal $$$ =================
                                            10/03/2026
      """)

renda_mensal = float(input("Digite sua renda mensal: "))
valor_do_emp = float(input("Digite o valor do empréstimo: "))
numero_de_prestacoes = int(input("Digite o número de prestações: "))


valor_prestacao = valor_do_emp / numero_de_prestacoes
limite_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30


if valor_do_emp <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print(Fore.GREEN + "Empréstimo Concedido")
else: 
    print(Fore.RED + "Empréstimo não concedido")
