a, b = map(int, input("").split())

if a % b == 0 or b % a == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")