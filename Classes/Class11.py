nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
carteira = input("Você tem carteira de motorista [S/N]: ").upper()

try:
    idade_int = int(idade)

    if idade_int >= 18:
        if carteira == "S":
            print(f"{nome}, você pode dirigir.")
        else:
            print(f"{nome}, você precisa de uma carteira de motorista para dirigir.")
    else:
        print(f"{nome}, você é menor de idade, não pode dirigir e muito menos tirar uma carteira.")

except ValueError:
    print("Idade inválida.")
