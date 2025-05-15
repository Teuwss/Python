a, b, c = map(int, input("").split())

if a < b and a < c:
    if b < c:
        print(f"{a}, {b}, {c} - {a}, {b}, {c}")
    else:
        print(f"{a}, {c}, {b} - {a}, {b}, {c}")

elif b < a and b < c:
    if a < c:
        print(f"{b}, {a}, {c} - {a}, {b}, {c}")
    else:
        print(f"{b}, {c}, {a} - {a}, {b}, {c}")

else:
    if a < b:
        print(f"{c}, {a}, {b} - {a}, {b}, {c}")
    else:
        print(f"{c}, {b}, {a} - {a}, {b}, {c}")

