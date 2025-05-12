valor = float(input())
valor = int(valor * 100)

n100 = valor // 10000
valor = valor % 10000

n50 = valor // 5000
valor = valor % 5000

n20 = valor // 2000
valor = valor % 2000

n10 = valor // 1000
valor = valor % 1000

n5 = valor // 500
valor = valor % 500

n2 = valor // 200
valor = valor % 200

n1 = valor // 100
valor = valor % 100

n_0_50 = valor // 50
valor = valor % 50

n_0_25 = valor // 25
valor = valor % 25

n_0_10 = valor // 10
valor = valor % 10

n_0_05 = valor // 5
valor = valor % 5

n_0_01 = valor // 1
valor = valor % 1

print("NOTAS:")
print(f"{int(n100)} nota(s) de R$ 100.00")
print(f"{int(n50)} nota(s) de R$ 50.00")
print(f"{int(n20)} nota(s) de R$ 20.00")
print(f"{int(n10)} nota(s) de R$ 10.00")
print(f"{int(n5)} nota(s) de R$ 5.00")
print(f"{int(n2)} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{int(n1)} moeda(s) de R$ 1.00")
print(f"{int(n_0_50)} moeda(s) de R$ 0.50")
print(f"{int(n_0_25)} moeda(s) de R$ 0.25")
print(f"{int(n_0_10)} moeda(s) de R$ 0.10")
print(f"{int(n_0_05)} moeda(s) de R$ 0.05")
print(f"{int(n_0_01)} moeda(s) de R$ 0.01")
