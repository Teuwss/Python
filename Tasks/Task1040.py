nota_1, nota_2, nota_3, nota_4 = map(float, input().split())

media = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 * 4) + (nota_4 * 1)) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
else:
    print("Aluno reprovado.")