print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
calculo = int(input("Digite a operação que você deseja realizar? "))
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o outro numero: "))
if calculo == 1:
  soma = numero1 + numero2
  print("O resultado é: ", soma)
elif calculo == 2:
  if numero1 < 0 and numero2 < 0:  
    subtracao = numero1 - (-numero2)  
  else:
    subtracao = numero1 - numero2
  print("O resultado é: ", subtracao)
elif calculo == 3:
  multiplicacao = numero1 * numero2
  print("O resultado é: ", multiplicacao)
elif calculo == 4:
  if numero2 == 0:
    print("Operação inválida")
  else:
    divisao = numero1 / numero2
    print("O resultado é", divisao)
else:
  print("Operação inválida.")