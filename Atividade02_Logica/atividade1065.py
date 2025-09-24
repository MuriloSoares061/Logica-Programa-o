# Lê numeros inteiros

valores = [int(input()) for _ in range(5)]

# Conta quantos são pares

pares = sum(1 for v in valores if v % 2 == 0)

# Saida 

print(f"{pares} valores pares")