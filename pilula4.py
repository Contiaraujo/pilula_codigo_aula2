import statistics as st

#entrada
lote1 = int(input("Produção Lote 1: "))
lote2 = int(input("Produção Lote 2: "))
lote3 = int(input("Produção Lote 3: "))
#processamento
media = st.mean((lote1,lote2,lote3) )
desvio = st.stdev((lote1,lote2,lote3))
#saida
print(f"Média: {media:.2f}")
print(f"Desvio Padrão: {desvio:2f}")