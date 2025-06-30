lista={}
def saudac():
    print('-' * 30)
    print('-' * 8 + 'MENU PRINCIPAL' + '-' * 8)
    print("Escolha a opção desejada:")
    print('1 - Cadastrar Livro')
    print('2 - consultar Livros')
    print('3 - Remover Livro')
    print('4 - Sair')
    print('-' * 30)




def cadastrar_livro():


    print('-' * 30)
    print('-' * 5 + 'MENU CADASTRAR LIVRO' + '-' * 5)
    while True:
         id = int(input("Digite o id do livro: "))  # Obtendo o ID único do livro

         # Criando uma nova lista para cada livro
         lista_livros = []

         nome = input("Entre com o nome do livro: ")
         lista_livros.append(nome)

         autor = input("Entre com o nome do autor: ")
         lista_livros.append(autor)

         editora = input("Entre com o nome da editora do livro: ")
         lista_livros.append(editora)

         # Adicionando ao dicionário
         lista[id] = lista_livros
         import csv



         with open("lista.csv", "w", newline="") as f:
             escritor = csv.DictWriter(f, fieldnames=lista[0].keys())
             escritor.writeheader()
             escritor.writerows(lista)

         perg = input("Deseja adicionar mais algum? (S/N)").lower()

         if perg == 'n':
            print(lista)
            return menu(lista)


def consultar_livro():
    print('-' * 30)
    print('-' * 9 + 'CONSULTAR' + '-' * 10)
    print("Escolha a opção desejada:")
    print("1 - Consultar todos os livros")
    print("2 - Consultar livros por ID")
    print("3 - Consultar livro(s) por autor")
    print("4 - Retornar")


    while True:
        try:
           opcao = int(input('Digite uma das opções do menu:  '))
           if opcao not in [1, 2, 3, 4]:
               print("Digite um numero inteiro entre 1 e 4 ")
               continue
           if opcao == 1:
             for keys,values in lista.items():
                  print(f"{keys}={values}")
           elif opcao ==2:
               id =int(input("Digite a id do livro: "))
               idf=lista.get(id,None)
               if idf is None:
                     print("A id não existe")
               else:
                   print(idf)
           elif opcao ==3:
                busca=input("Digite o nome do autor: ")
                for livro, valores in lista.items():
                   if busca in valores:
                      print(lista[livro])
                break
           elif opcao ==4:
               return menu(lista)
        except:
            print("valor incorreto")
            print("Digite um numero inteiro entre 1 e 4 ")



def remover():
    print('-' * 30)
    print('-' * 6 + 'MENU REMOVER LIVRO' + '-' * 6)
    remove = int(input("Digite o id do livro a ser removido: "))
    while remove not in [1, 2, 3, 4]:
        print('este numero não corresponde ao ID, digite um id valido')
        remove = int(input("Digite o id do livro a ser removido: "))
    removido = lista.pop(remove)
    print(f"O livro removido foi {removido}")
    print("livro removido com sucesso!")
    print(lista)
    return menu(lista)





def menu(lista):
    menu = saudac()
    print(menu)

    while True:
        try:
            opc = int(input("Digite aqui sua escolha: "))
            if opc not in [1, 2, 3, 4]:
                continue
            else:
                if opc == 1:
                    cadastrar_livro()

                elif opc == 2:
                    consultar_livro()
                elif opc == 3:
                    return remover()

                elif opc == 4:
                    print("Obrigado por visitar nossa Biblioteca,volte sempre!")

                break  # este break está aqui temporariamente,pois posteriormente vai ser deslocado
        except:
            print("Digite um numero inteiro entre 1 e 4 ")


# Programa principal
saida = menu(lista)
print(saida)

