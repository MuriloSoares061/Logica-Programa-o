# Dados de entrada

dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))

dia_termino = int(input().split()[1])
hora_termino, minuto_termino, segundo_termino = map(int,input().split(" : "))

# Conversão para segundos

segundos_total_inicio = (dia_inicio * 86400) + (hora_inicio * 3600) + (minuto_inicio * 60) + segundo_inicio
segundos_total_termino = (dia_termino * 86400) + (hora_termino * 3600) + (minuto_termino * 60) + segundo_termino

# Cálculo da duração
duracao_segundos = segundos_total_termino - segundos_total_inicio

# Conversão da duração de volta para dias, horas, minutos e segundos
dias = duracao_segundos // 86400
resto = duracao_segundos % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

# Impressão da saída
print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')