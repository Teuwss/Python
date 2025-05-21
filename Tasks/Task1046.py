hora_inicial, hora_final = map(int, input("").split())

if hora_final > hora_inicial:
    print(f"O jogo durou {hora_final - hora_inicial} horas")
else:
    print(f"O jogo durou {(24 - hora_inicial) + hora_final} horas")
