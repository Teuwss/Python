a, b, c = map(float, input("").split())

if b > a:
    a, b = b, a
if c > a:
    a, c = c, a

if a >= b + c:
    print(f"Não forma triangulo")

if a ** 2 == b ** + c ** 2:
    print(f"Triangulo retangulo")

if a ** 2 > b ** + c ** 2:
    print("Triangulo obtusangulo")

if a ** 2 < b ** + c ** 2:
    print(f"Triangulo acutangulo")

if a == b == c:
    print(f"Triangulo equilatero")

if a == b or a == c or c == b:
    print(f"Triangulo isosceles")
