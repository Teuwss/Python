idade = int(input("Sua idade: "))  # Solicita a idade do usuário.
carteira = input("Tem carteira de motorista? (S/N): ")  # Pergunta se possui carteira.

# Verifica se a pessoa tem 18 anos ou mais E tem carteira.
if idade >= 18 and carteira == "S":
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")
