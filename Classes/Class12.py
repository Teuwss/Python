usuario_logado = None

nome = input("Digite seu nome: ")

if nome == "Admin":
    usuario_logado = nome
    if usuario_logado is not None:
        print("Você está logado.")
    else:
        print("Você não está logado")
else:
    print(f"Bem vindo, {nome}")