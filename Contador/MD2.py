def fração(n):
    p = 1
    q = 1
    contador = 1
    while contador < n:

        if (p == 1) and (q % 2 == 1):
            contador += 1
            q += 1
        elif (p == 1) and (q % 2 == 0):
            while (q > 1) and contador < n:
                p += 1
                q -= 1
                contador += 1
        elif (q == 1) and (p % 2 == 0):
            p += 1
            contador += 1 
        elif (q == 1) and (p % 2 == 1):
            while p > 1 and contador < n:
                p -= 1
                q += 1
                contador += 1
                
    return p, q
resultado = fração(1000000)
print(resultado)