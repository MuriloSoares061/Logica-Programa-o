# Imposto da Cidade 

rombus = float(input())

if rombus <= 2000.00:
    print("Isento")
elif rombus <= 3000.00:
    imposto = (rombus - 2000.00) * 0.08
    print(f"R${imposto:.2f}")
elif rombus <= 4500.00:
    imposto = 80.00 + (rombus - 3000.00) * 0.18
    print(f"R${imposto:.2f}")
else:
    imposto = 80.00 + 270.00 + (rombus - 4500) * 0.28
    print(f"R${imposto:.2f}")