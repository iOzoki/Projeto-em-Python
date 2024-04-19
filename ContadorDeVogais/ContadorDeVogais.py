x = 0
frase = input("Digite a frase: ")
for letras in frase:
  letras = letras.lower()
  if letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u":
   x = x + 1
print(x)