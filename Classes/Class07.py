# Pergunta ao usuário se ele quer entrar ou sair
verificar = input("Você quer 'Entrar' ou 'Sair'? ")

# Verifica se o usuário digitou 'Entrar'
if verificar == "Entrar":
    print("Você entrou.")
    
# Se não, verifica se ele digitou 'Sair'
elif verificar == "Sair":
    print("Você saiu.")

# Se não digitou nem 'Entrar' nem 'Sair'
else:
    print("Você não digitou nem 'Entrar' e nem 'Sair'.")
