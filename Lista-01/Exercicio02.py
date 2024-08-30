#2. Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar ou par.

num =  int(input("Digite um numero: "))

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é impar")