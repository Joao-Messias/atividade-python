import db
import file_manager
import csv_manager

def menu():
    print("\nSistema de Gerenciamento de Livraria")
    print("1. Adicionar novo livro")
    print("2. Exibir todos os livros")
    print("3. Atualizar preço de um livro")
    print("4. Remover um livro")
    print("5. Buscar livros por autor")
    print("6. Exportar dados para CSV")
    print("7. Importar dados de CSV")
    print("8. Fazer backup do banco de dados")
    print("9. Sair")
    return input("Escolha uma opção: ")

def executar():
    file_manager.criar_diretorios()
    db.criar_tabela()

    while True:
        opcao = menu()

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de publicação: "))
            preco = float(input("Preço: "))
            db.adicionar_livro(titulo, autor, ano, preco)
            file_manager.fazer_backup()

        elif opcao == '2':
            livros = db.listar_livros()
            for livro in livros:
                print(livro)

        elif opcao == '3':
            livro_id = int(input("ID do livro: "))
            novo_preco = float(input("Novo preço: "))
            db.atualizar_preco(livro_id, novo_preco)
            file_manager.fazer_backup()

        elif opcao == '4':
            livro_id = int(input("ID do livro: "))
            db.remover_livro(livro_id)
            file_manager.fazer_backup()

        elif opcao == '5':
            autor = input("Nome do autor: ")
            livros = db.buscar_por_autor(autor)
            for livro in livros:
                print(livro)

        elif opcao == '6':
            csv_manager.exportar_para_csv()

        elif opcao == '7':
            file_path = input("Caminho do arquivo CSV: ")
            csv_manager.importar_de_csv(file_path)
            file_manager.fazer_backup()

        elif opcao == '8':
            file_manager.fazer_backup()

        elif opcao == '9':
            break

        else:
            print("Opção inválida!")

if __name__ == '__main__':
    executar()
