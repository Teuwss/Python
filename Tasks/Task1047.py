hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input("").split())

inicio_total = hora_inicial * 60 + minuto_inicial
fim_total = hora_final * 60 + minuto_final

if fim_total > inicio_total:
    duracao = fim_total - inicio_total
else:
    duracao = (24 * 60 - inicio_total)

horas = duracao // 60

minutos = duracao % 60

print(f"O jogo durou {horas} horas e {minutos} minutos")
