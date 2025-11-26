while True:
    soma = 0
    qtd_validas = 0

    # 1. Loop para pegar as duas notas válidas
    while qtd_validas < 2:
        nota = float(input())
        
        if 0 <= nota <= 10:
            soma += nota
            qtd_validas += 1
        else:
            print("nota invalida")

    # 2. Calcula e mostra a média
    media = soma / 2
    print(f"media = {media:.2f}")

    # 3. Loop do menu para um novo calculo
    codigo = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        codigo = int(input())

        if codigo == 1:
            break  # Sai do loop do menu e reinicia o loop principal
        elif codigo == 2:
            break  # Quebra o loop do menu 

    if codigo == 2:
        break