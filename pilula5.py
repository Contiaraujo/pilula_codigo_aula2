import locale
#entrada
locale.setlocale(locale.LC_ALL,"pt_BR.UTF-8")
r1 = float(input("Receita Mês 1: "))
r2 = float(input("Receita Mês 2: "))
r3 = float(input("Receita Mês 3: "))
#processamento
total = r1+r2+r3
#saida
print(f"Mês 1: {locale.currency(r1, grouping=True)}")
print(f"Mês 2: {locale.currency(r2, grouping=True)}")
print(f"Mês 3: {locale.currency(r3, grouping=True)}")
print(f"Total: {locale.currency(total, grouping=True)}")
