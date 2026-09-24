produtos = {
    "arroz": {"preco": 10.0, "estoque": 50},
    "feijao": {"preco": 8.0, "estoque": 40},
    "macarrao": {"preco": 5.0, "estoque": 60},
}


def aplicar_desconto(total):
    if total >= 1000:
        return total * 0.85
    if total >= 500:
        return total * 0.90
    if total >= 200:
        return total * 0.95
        return total

vendas = []
clientes = []
resumo_vendas = []

while True:
    cliente = input("Nome do cliente: ")
    total = 0

    while True:
        print("Produtos:")
        for nome, p in produtos.items():
            print("- ", nome, "| R$", p["preco"], "| estoque:", p["estoque"])

        nome_produto = input("Produto (ou 'fim'): ").lower()

        if nome_produto == "fim":
            break

        if nome_produto not in produtos:
            print("Produto não encontrado!")
            continue

        qtd = int(input("Quantidade: "))
        produto = produtos[nome_produto]

        if qtd > produto["estoque"]:
            print("Estoque insuficiente!")
            continue

        total += produto["preco"] * qtd
        produto["estoque"] -= qtd

    total = aplicar_desconto(total)

    vendas.append(total)
    clientes.append(cliente)
    resumo_vendas.append({"cliente": cliente, "total": total})

    print("Total da compra com desconto: R$", total)

    if input("Nova venda? (s/n): ").lower() != "s":
        break


print("RELATÓRIO FINAL")
print("Total de vendas:", len(vendas))
print("Faturamento total: R$", sum(vendas))

if vendas:
    print("Cliente que mais comprou:", clientes[vendas.index(max(vendas))])
    print("Média das vendas:", sum(vendas) / len(vendas))

print("---- RESUMO DAS VENDAS ----")
for v in resumo_vendas:
    print("Cliente:", v["cliente"], "| Total:", v["total"])