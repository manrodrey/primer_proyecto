def arrow (n):
    for i in range(n):
        if i == n-1:
            print((2*n) * "*", end = " ") # fila del centro, pinta la cola entera
            print((i+1) * "*") # fila del centro, pinta la primera parte de la cola
        else:
            print((2*n) * " ", end = " ") # Esto pinta los espacios de la primera parte de la flecha
            print((i+1) * "*") # Pinta toda la primera parte de la flecha

    for j in range(n-1,0,-1): # Este for es para la parte de abajo de la flecha
        print((2*n) * " ", end = " ")
        print(j * "*")

arrow(4)