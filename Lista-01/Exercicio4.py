#4. Escreva um programa que leia a quantidade em segundos e imprima o resultado em dias,horas, minutos e segundos.

sec = int(input("Digite os segundos: "))

dias = sec // 86400
restosec = (sec % 60)
horas = restosec // 3600
minutos = (restosec // 60)
#restosec = (sec % 60)

print(f"{dias}:{horas}:{minutos}:{restosec}")