conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado_1 = conjunto_a.issuperset(conjunto_b) # False
resultado_2 = conjunto_b.issuperset(conjunto_a) # True

print(resultado_1, resultado_2)