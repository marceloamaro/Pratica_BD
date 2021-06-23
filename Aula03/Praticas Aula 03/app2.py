import data2


MENU_PROMPT = """
LINGUAGENS APP
Por favor, escolha uma das opções:
1) Adicione uma nova linguagem
2) Veja todas as linguagens
3) Encontre uma linguagem por nome 
4) Veja qual a linguagem mais antiga
5) Veja qual a linguagem mais recentes
6) Sair
"""
def menu():
    conexao = data2.connect()
    #data2.create(conexao)  # comentar essa linha depois de criar a tabela

    while(user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            nome = input("entre com o nome da linguagem:")
            criador = input("Nome do criador da linguagem:")
            ano = int(input("ano de criação da linguagem:"))

            data2.insert(conexao, nome, criador, ano)
           
        elif user_input == "2":
            linguagens =  data2.busca(conexao)

            for linguagem   in linguagens:
                print(f'Nome: {linguagem[1]} Criador: {linguagem[2]} ano:{linguagem[3]}')
        elif user_input == "3":
            nome = input("entre com sua busca: ")
            linguagens = data2.busca_nome(conexao, nome)

            for linguagem in linguagens:
                print(f'{linguagem[1]} {linguagem[2]} {linguagem[3]}' )

        elif user_input == "4":

            antiga = data2.busca_antiga(conexao)

            print(f'A linguagens mais antiga é  {antiga[1]} {antiga[2]} {antiga[3]}')

        elif user_input == "5":

            recente = data2.busca_recente(conexao)

            print(f'A linguagens mais recentes é  {recente[1]} {recente[2]} {recente[3]}')

        elif user_input == "6":
            exit()
        else:
            print("entrada inválida")

menu()