segundos = int(input(""))

horas = (segundos - (segundos % 3600)) // 3600
segundos = segundos % 3600

minutos = (segundos - (segundos % 60)) // 60
segundos = segundos % 60

segundos = segundos % 60

print(f"{horas}:{minutos}:{segundos}")