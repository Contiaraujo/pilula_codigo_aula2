import random
#entradas
cotacao = float(input("cotação atual do dolar: "))
#processamento
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
#saida
print(f"Variação Simulada: {variacao:.3%}")
print(f"Nova cotação: {nova_cotacao:.4f}")
