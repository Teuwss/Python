a, b, c = map(int, input("").split())

maior_ab = (a + b + abs (a - b)) // 2

maior_abc = (maior_ab + c + abs(maior_ab - c)) // 2

print(f"{maior_abc} é o maior número.")