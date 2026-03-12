import datetime

#entrada
data_compra = input("Digire a data da compra d/m/aaa: ")
meses = int(input("Prazo da garantia: "))
#processamento
data_inicial = datetime.datetime.strptime(data_compra, "%d/%m/%Y")
data_final = data_inicial + datetime.timedelta(days=meses * 30)
#saida
print(f"Garantia Válida até: {data_final.strftime("%d/%m/%Y")}")
print(f"Dia da semana: {data_final.strftime("%A")}")