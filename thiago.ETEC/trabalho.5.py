# Classe Produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Método para exibir os dados
    def exibir_dados(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}")


# Lista para armazenar os produtos
produtos = []


# Função para cadastrar produto
def cadastrar_produto():
    print("\n=== Cadastro de Produto ===")

    try:
        nome = input("Digite o nome do produto: ")

        preco = float(input("Digite o preço do produto: R$ ").replace(",", "."))

        if preco < 0:
            print("O preço não pode ser negativo.")
            return

        # Criando objeto Produto
        produto = Produto(nome, preco)

        # Adicionando na lista
        produtos.append(produto)

        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Erro: Digite um valor numérico válido para o preço.")


# Função para listar produtos
def listar_produtos():
    print("\n=== Lista de Produtos ===")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Agora a numeração começa em 1
    for i, produto in enumerate(produtos, start=1):
        print(f"{i} - {produto.nome} | R$ {produto.preco:.2f}")


# Função para comprar produto
def comprar_produto():
    print("\n=== Compra de Produto ===")

    if len(produtos) == 0:
        print("Nenhum produto disponível para compra.")
        return

    listar_produtos()

    try:
        indice = int(input("Digite o número do produto: "))

        # Verifica se o número existe
        if indice < 1 or indice > len(produtos):
            print("Produto inexistente.")
            return

        quantidade = int(input("Digite a quantidade: "))

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return

        # Ajuste do índice da lista
        produto = produtos[indice - 1]

        total = produto.preco * quantidade

        print(f"\nProduto escolhido: {produto.nome}")
        print(f"Quantidade: {quantidade}")
        print(f"Total a pagar: R$ {total:.2f}")

        # Expressões relacionais e lógicas
        if total >= 100:
            print("Desconto disponível!")
        else:
            print("Sem desconto.")

    except ValueError:
        print("Erro: Digite apenas números válidos.")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")


# Programa principal
while True:
    print("\n========= MENU =========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produto")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        comprar_produto()

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")