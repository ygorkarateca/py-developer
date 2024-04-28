conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado_1 = conjunto_a.isdisjoint(conjunto_b) # True
resultado_2 = conjunto_a.isdisjoint(conjunto_c) # False

print(resultado_1, resultado_2)