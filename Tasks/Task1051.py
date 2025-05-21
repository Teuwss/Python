renda = float(input())

imposto = 0

if renda <= 2000.00:
    print("Isento")
elif renda <= 3000.00:
    imposto = (renda - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
elif renda <= 4500.00:
    imposto = (1000.00 * 0.08)
    imposto += (renda - 3000.00) * 0.18
    print(f"R$ {imposto:.2f}")
else:
    imposto = (1000.00 * 0.08)
    imposto += (1500.00 * 0.18)
    imposto += (renda - 4500.00) * 0.28
    print(f"R$ {imposto:.2f}")
