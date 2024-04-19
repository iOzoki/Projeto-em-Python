#Um software comercial necessita de um sistema de segurança que protege a emissão de relatórios confidenciais. O software deve solicitar o numero da matrícula e a senha do funcionário e só então liberar o acesso
matricula1 = 987
matricula2 = 321
matricula3 = 654
senha1 = 789
senha2 = 123
senha3 = 456
num_matricula = int(input("Digite o número da matrícula: "))
num_senha = int(input("Digite o número da senha: "))
if num_matricula == matricula1 and num_senha == senha1 or num_matricula == matricula2 and num_senha == senha2 or num_matricula == matricula3 and num_senha == senha3:
  print("Acesso liberado!")
else:
  print("Acesso negado!")