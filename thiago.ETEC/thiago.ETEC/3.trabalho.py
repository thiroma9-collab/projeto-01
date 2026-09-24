produtos = [
    {"nome": "arroz", "preco": 10.0, "estoque": 50},
    {"nome": "feijao", "preco": 8.0, "estoque": 40},
    {"nome": "macarrao", "preco": 5.0, "estoque": 60},
]

def calcular_subtotal(preco, quantidade):
    return preco * quantidade


def aplicar_desconto(total):
    if total >= 1000:
        return total * 0.85
    elif total >= 500:
        return total * 0.90
    elif total >= 200:
        return total * 0.95
    else:
        return total


def calcular_media(vendas):
    return sum(vendas) / len(vendas)


def maior_compra(vendas, clientes):
    maior = max(vendas)
    indice = vendas.index(maior)
    return clientes[indice]


vendas = []
clientes = []
resumo_vendas = []

while True:
    nome_cliente = input("Nome do cliente: ")
    total_venda = 0

    while True:
        print("Produtos disponíveis:")
        for p in produtos:
            print("- ", p["nome"], "| R$", p["preco"], "| estoque:", p["estoque"])

        produto_nome = input("Digite o nome do produto (ou 'fim'): ")

        if produto_nome == "fim":
            break

        produto_encontrado = None

        for p in produtos:
            if p["nome"] == produto_nome:
                produto_encontrado = p

        if produto_encontrado:
            qtd = int(input("Quantidade: "))

            if qtd <= produto_encontrado["estoque"]:
                subtotal = calcular_subtotal(produto_encontrado["preco"], qtd)
                total_venda += subtotal
                produto_encontrado["estoque"] -= qtd
            else:
                print("Estoque insuficiente!")
        else:
            print("Produto não encontrado!")

    total_final = aplicar_desconto(total_venda)

    vendas.append(total_final)
    clientes.append(nome_cliente)

    resumo_vendas.append({
        "cliente": nome_cliente, 
        "total": total_final
    })

    print("Total da compra com desconto: R$", total_final)

    continuar = input("Nova venda? (s/n): ")
    if continuar.lower() != "s":
        break

print("RELATÓRIO FINAL")

print("Total de vendas:", len(vendas))

faturamento = sum(vendas)
print("Faturamento total: R$", faturamento)

if vendas:
    print("Cliente que mais comprou:", maior_compra(vendas, clientes))
    print("Média das vendas:", calcular_media(vendas))

print("---- RESUMO DAS VENDAS ----")
for v in resumo_vendas:
    print("Cliente:", v["cliente"], "| Total:", v["total"])