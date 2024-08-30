'''3. Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, ecalcule as raízes x’ e x”
    através da fórmula de Báskara.'''
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = ((b ** 2) - 4* a * c)
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"raíz x': {x1}")
print(f"raíz x'': {x2} " )