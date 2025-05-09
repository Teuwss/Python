codigo_peca1, numero_peca1, valor_da_peca1 = input("").split()
codigo_peca1 = int(codigo_peca1)
numero_peca1 = int(numero_peca1)
valor_da_peca1 = float(valor_da_peca1)

codigo_peca2, numero_peca2, valor_da_peca2 = input("").split()
codigo_peca2 = int(codigo_peca2)
numero_peca2 = int(numero_peca2)
valor_da_peca2 = float(valor_da_peca2)

valor_a_pagar = numero_peca1 * valor_da_peca1 + numero_peca2 * valor_da_peca2

print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")


