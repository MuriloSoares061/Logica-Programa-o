x = int(input())
y = int(input())

soma = 0

# 1. Garantir que o X seja o menor e o Y o maior.
# Se X for maior que Y, nós trocamos os valores usando uma variável auxiliar.
if x > y:
    aux = x
    x = y
    y = aux

# Agora temos certeza que o intervalo vai de X até Y.

# 2. Usar WHILE para percorrer os números
atual = x
while atual <= y:
    # Verifica se NÃO é divisível por 13
    if atual % 13 != 0:
        soma = soma + atual
    
    # É obrigatório aumentar o valor manualmente no while
    atual = atual + 1

print(soma)