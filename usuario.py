nome = input("Qual seu nome de usuário? ")
senha = input ("Informe sua senha: ")
   
while senha == nome:
    print ("Erro: Sua senha não pode ser seu nome de usuário.")
    senha = input ("Digite uma senha:")
else: 
    print('Login feito com sucesso!')