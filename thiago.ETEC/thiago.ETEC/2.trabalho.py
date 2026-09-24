def cadastrar_produtos():
    produtos = []

    qtd = int(input("Quantos produtos serão cadastrados? "))

    for i in range(qtd):
        print(f"Produto {i + 1}")
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Quantidade em estoque: "))

        produto = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }

        produtos.append(produto)

    return produtos


def buscar_produto(produtos, nome):
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            return produto
    return None


def calcular_desconto(total):
    if total >= 1000:
        return total * 0.15
    elif total >= 500:
        return total * 0.10
    elif total >= 200:
        return total * 0.05
    else:
        return 0


produtos = cadastrar_produtos()

cliente = input("Nome do cliente: ")

total_compra = 0
compras = []

continuar = "S"

while continuar != "N":

    nome_prod = input("Nome do produto desejado: ")
    produto = buscar_produto(produtos, nome_prod)

    if produto is None:
        print("Produto não encontrado!")
    else:
        qtd = int(input("Quantidade desejada: "))

        if qtd <= produto["estoque"]:
            subtotal = qtd * produto["preco"]
            total_compra += subtotal

            produto["estoque"] -= qtd

            compras.append({
                "nome": produto["nome"],
                "quantidade": qtd,
                "subtotal": subtotal
            })

            print(f"Subtotal: R$ {subtotal:.2f}")
        else:
            print("Quantidade indisponível em estoque!")

    continuar = input("Deseja continuar comprando? (S/N): ").upper()


desconto = calcular_desconto(total_compra)
total_final = total_compra - desconto

print("========== RESUMO DA COMPRA ==========")
print(f"Cliente: {cliente}")

print("Produtos comprados:")
for item in compras:
    print(f"- {item['nome']} | Qtd: {item['quantidade']} | Subtotal: R$ {item['subtotal']:.2f}")

print(f"Total da compra: R$ {total_compra:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total final: R$ {total_final:.2f}")