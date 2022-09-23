opcao_do_menu = 0 

def menu():
#Criando um menu de opções
 print('''\nSelecione o que quer fazer:
 1 - Incluir nova tarefa,
 2 - Ver lista de tarefas,
 3 - Excluir tarefa salva,
 4 - Sair
 ''')

  #Receber a opção do usuario
menu()
opcao_do_menu = int(input('Qual o número ação você quer fazer? '))
lista_de_tarefas = []

while True:
    if opcao_do_menu == 1:
        print('Opção escolhida: 1 - Incluir nova tarefa.')
        opcao_do_menu = 0
        tarefa = input('\nDigite tarefa a ser adicionada: ')
        lista_de_tarefas.append(tarefa)
        print('\nSua lista de tarefas')
        print(lista_de_tarefas)
        menu()
        opcao_do_menu = input('Qual o número ação você quer fazer? ')

    elif opcao_do_menu == 2:
        print('Opção escolhida: 2 - Ver lista de tarefa.')
        opcao_do_menu = 0
        print('\nSua lista de tarefas')
        print(lista_de_tarefas)
        menu()
        opcao_do_menu = int(input('Qual o número ação você quer fazer? '))    

    elif opcao_do_menu == 3:
        print('Opção escolhida: 3 - Excluir tarefa salva.')
        opcao_do_menu = 0
        print(lista_de_tarefas)
        tarefaremovida = str(input('Qual tarefa você deseja remover? '))
        lista_de_tarefas.remove(tarefaremovida)
        print(lista_de_tarefas)
        menu()
        opcao_do_menu = int(input('Qual o número ação você quer fazer? '))    

    elif opcao_do_menu == 4:
         print('Opção escolhida: 4 - Sair.')
         respostadesaida = str(input('Quer mesmo sair? S/N ').upper())
         if (respostadesaida == 'S') or (respostadesaida == 'SIM'):
            break
         else: 
            print('\n')
            menu()
            opcao_do_menu = int(input('Qual o número ação você quer fazer? '))    
