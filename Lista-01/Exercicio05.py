#5. Escreva um programa que converta uma temperatura digitada em "C” em “F”.

temp_celsius = int(input("Digite a temperatura em Celsius: "))

Conversor = (temp_celsius * (9/5)) + 32
print(f"{Conversor}")