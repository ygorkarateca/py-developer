conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado_1 = conjunto_a.issubset(conjunto_b) # True
resultado_2 = conjunto_b.issubset(conjunto_a) # False

print(resultado_1, resultado_2)