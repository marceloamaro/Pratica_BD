import data


MENU_PROMPT = """
LINGUAGENS APP
Por favor, escolha uma das opções:
1) Adicione uma nova linguagem
2) Veja todas as linguagens
3) Encontre uma linguagem por nome 
4) Veja qual a linguagem mais antiga
5) Sair
"""
def menu():
    conexao = data.connect()
    data.create(conexao)  # comentar essa linha depois de criar a tabela

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            nome = input("entre com o nome da linguagem")
            criador = input("Nome do criador da linguagem")
            ano = int(input("ano de criação da linguagem"))

            data.insert(conexao, nome, criador, ano)
           
        elif user_input == "2":
            linguagens =  data.busca(conexao)

            for linguagem   in linguagens:
                print(f'Nome: {linguagem[1]} Criador: {linguagem[2]} ano:{linguagem[3]}')
        elif user_input == "3":
            nome = input("entre com sua busca: ")
            linguagens = data.busca_nome(conexao, nome)

            for linguagem in linguagens:
                print(f'{linguagem[1]} {linguagem[2]} {linguagem[3]}' )

        elif user_input == "4":

            antiga = data.busca_antiga(conexao)

            print(f'A linguagens mais antiga é  {antiga[2]}')
        elif user_input == "5":
            exit()
        else:
            print("entrada inválida")

menu()