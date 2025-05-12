valor = int(input(""))

n100 = (valor - (valor % 100)) // 100
valor = valor % 100

n50 = (valor - (valor % 50)) // 50
valor = valor % 50

n20 = (valor - (valor % 20)) // 20
valor = valor % 20

n10 = (valor - (valor % 10)) // 10
valor = valor % 10

n5 = (valor - (valor % 5)) // 5
valor = valor % 5

n2 = (valor - (valor % 2)) // 2
valor = valor % 2

n1 = (valor - (valor % 1)) // 1
valor = valor % 1

print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")