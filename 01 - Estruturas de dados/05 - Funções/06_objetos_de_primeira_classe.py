def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operacao é = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operacao 10 + 10 = 20
exibir_resultado(10, 10, subtrair) # O resultado da operacao 10 - 10 = 0


op1 = somar
print(op1(1, 34))

op2 = subtrair
print(op2(3, 2))