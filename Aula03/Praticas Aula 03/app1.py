import data1


MENU_PROMPT = """
AGENDA APP
Por favor, escolha uma das opções:
1) Adicione um novo contato
2) Veja todos contatos
3) Encontre um contato por nome 
4) Veja qual contato add mais antiga
5) Veja qual contato add mais recentes
6) Sair
"""
def menu():
    conexao = data1.connect()
    #data1.create(conexao)  # comentar essa linha depois de criar a tabela

    while(user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            nome = input("entre com o nome do contato:")
            telefone = input("Numero do telefone:")
            

            data1.insert(conexao, nome, telefone)
           
        elif user_input == "2":
            dado =  data1.busca(conexao)

            for agenda   in dado:
                print(f'Nome: {agenda[1]} telefone: {agenda[2]}')
        elif user_input == "3":
            nome = input("entre com sua busca: ")
            dado = data1.busca_nome(conexao, nome)

            for agenda in dado:
                print(f'{agenda[1]} {agenda[2]}' )

        elif user_input == "4":

            antiga = data1.busca_antiga(conexao)

            print(f'O contato add mais antigo é  {antiga[1]} {antiga[2]} ')

        elif user_input == "5":

            recente = data1.busca_recente(conexao)

            print(f'O contato add recente é  {recente[1]} {recente[2]} ')

        elif user_input == "6":
            exit()
        else:
            print("entrada inválida")

menu()