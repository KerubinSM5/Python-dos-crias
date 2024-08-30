#1. Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do usuário essesnúmeros e imprime sua soma,
#    produto, diferença e divisão.

num = int(input("Adicione o primeiro numero: "))
num2 = int(input("Adicione o segundo numero: "))

soma = num + num2
diferenca = num - num2
produto = num * num2
divisao = num / num2

print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")
print(f"Divisao: {divisao}")