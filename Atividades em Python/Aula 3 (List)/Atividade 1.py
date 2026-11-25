meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
temperaturas = []
regiA = {}
for i in range(12):
    t = float(input("Temperatura de " + meses[i] + ": "))
    temperaturas += [t]
    regiA[meses[i]] = t
med = sum(temperaturas) / 12
print(f"\nMédia anual: {med}")
print("\nMeses acima da média:")
for i in range(12):
    mesatual = meses[i]
    tempatual = regiA[mesatual]
    if tempatual > med:
        print(i + 1, "-",mesatual, ":",tempatual)