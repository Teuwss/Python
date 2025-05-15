codigo, quantidade = map(int, input("").split())

if codigo == 1:
    codigo = 4.00
elif codigo == 2:
    codigo = 4.50
elif codigo == 3:
    codigo = 5.00
elif codigo == 4:
    codigo = 2.00
elif codigo == 5:
    codigo = 1.50
else:
    print("As opções são de 1 à 5")

total = codigo * quantidade

print(f"Total: R$  {total:.2f}")