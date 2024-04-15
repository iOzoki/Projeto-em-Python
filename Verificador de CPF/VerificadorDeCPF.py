def valida_cpf(cpf):

    if len(cpf) != 11 or not cpf.isdigit():
        return False
    

    digitos = [int(d) for d in cpf]
    

    p1 = sum((10 - k) * digitos[k] for k in range(9))
    r1 = p1 % 11
    

    if r1 < 2:
        if digitos[9] != 0:
            return False
    else:
        if digitos[9] != (11 - r1):
            return False


    p2 = sum((11 - k) * digitos[k] for k in range(10))
    r2 = p2 % 11
    

    if r2 < 2:
        if digitos[10] != 0:
            return False
    else:
        if digitos[10] != (11 - r2):
            return False
    

    return True


cpf = "14031758456" 

if valida_cpf(cpf):
    print("CPF Válido")
else:
    print("CPF Não Válido")