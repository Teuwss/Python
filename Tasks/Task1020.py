dias = int(input(""))

anos = (dias - (dias % 365)) // 365
dias = dias % 365

meses = (dias - (dias % 30)) // 30
dias = dias % 30

print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s)")
