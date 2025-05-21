salario = float(input(""))

if salario <= 400.00:
    reajuste = salario * 0.15
    percentual = 15
elif salario <= 800.00:
    reajuste = salario * 0.12
    percentual = 12
elif salario <= 1200.00:
    reajuste = salario * 0.10
    percentual = 10
elif salario <= 2000.00:
    reajuste = salario * 0.7
    percentual = 7
else:
    reajuste = salario * 0.4
    percentual = 4

print(f"Novo salario: {salario + reajuste:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %")
