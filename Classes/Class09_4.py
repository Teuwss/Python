nome = input("")

if "a" in nome or "A" in nome:
    print("A letra 'a' está presente no seu nome.")
else:
    print("A letra 'a' não está no seu nome.")

senha = input("")

if not "123" in senha:
    print("Senha segura.")
else:
    print("Senha fraca. Evite usar números sequenciais.")