# Lê os numeros

N = int(input())

# Contador

dentro = 0
fora = 0

# Loop para ler N

for i in range(N):
    X = int(input())
    if 10 <= X <= 20:
        dentro += 1
    else:
        fora += 1

# Saida

print(f"{dentro} in")
print(f"{fora} out")