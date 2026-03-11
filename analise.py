import csv

valores = []

with open("gastos.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        valores.append(float(linha["valor"]))

total = sum(valores)
media = total / len(valores)
maior = max(valores)

print("Análise de gastos")
print("Total gasto:", total)
print("Média de gastos:", media)
print("Maior gasto:", maior)
