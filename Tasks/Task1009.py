nome = input("")
salario = float(input(""))
total_vendas = float(input(""))

comissao = total_vendas * 0.15

novo_salario = comissao + salario

print(f"TOTAL = R$ {novo_salario:.2f}")
