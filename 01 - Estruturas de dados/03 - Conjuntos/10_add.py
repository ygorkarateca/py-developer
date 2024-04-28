sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 42, 25, ,23}
sorteio.add(25) #  {1, 42, 25, 23}

print(sorteio)