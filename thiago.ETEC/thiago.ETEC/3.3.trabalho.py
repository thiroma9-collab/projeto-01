produtos = []

while True:
    print("\n=== CADASTRO DE PRODUTO ===")

    nome = input("Nome do produto: ")

    # -------------------------
    # VALIDAÇÃO DO PREÇO (AJUSTE IMPORTANTE)
    # -------------------------
    while True:
        preco = input("Preço do produto: ").replace(",", ".")

        try:
            preco = float(preco)

            if preco >= 0:
                break
            else:
                print("Digite um valor maior ou igual a 0!")

        except ValueError:
            print("Valor inválido! Digite um número válido (ex: 10.99 ou 10,99).")

    estoque = int(input("Estoque: "))

    produtos.append({
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    })

    continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()

    if continuar != "s":
        break


# -------------------------
# FUNÇÕES
# -------------------------
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
    if len(vendas) == 0:
        return 0

    total = 0
    for v in vendas:
        total += v["total"]

    return total / len(vendas)


def maior_compra(vendas):
    maior = vendas[0]
    for v in vendas:
        if v["total"] > maior["total"]:
            maior = v
    return maior


def buscar_produto(nome):
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            return p
    return None


# -------------------------
# PARTE 2 - VENDAS
# -------------------------
vendas = []
total_faturado = 0

while True:
    print("\n=== NOVA VENDA ===")
    cliente = input("Nome do cliente: ")

    total_venda = 0

    # LOOP DE ITENS COM VALIDAÇÃO s/n
    while True:
        continuar_itens = input("\nQuer acrescentar um produto? (s/n): ").lower()

        if continuar_itens not in ["s", "n"]:
            print("Entrada inválida! Digite s/n.")
            continue

        if continuar_itens == "n":
            break

        nome_produto = input("Nome do produto: ")

        produto = buscar_produto(nome_produto)

        if produto is None:
            print("Produto não encontrado!")
            continue

        quantidade = int(input("Quantidade: "))

        if quantidade <= 0 or quantidade > produto["estoque"]:
            print("Quantidade inválida ou estoque insuficiente!")
            continue

        subtotal = calcular_subtotal(produto["preco"], quantidade)
        total_venda += subtotal

        produto["estoque"] -= quantidade

        print(f"Subtotal: R$ {subtotal:.2f}")

    # -------------------------
    # DESCONTO
    # -------------------------
    total_com_desconto = aplicar_desconto(total_venda)

    print(f"\nTotal sem desconto: R$ {total_venda:.2f}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")

    vendas.append({
        "cliente": cliente,
        "total": total_com_desconto
    })

    total_faturado += total_com_desconto

    # -------------------------
    # NOVA VENDA
    # -------------------------
    nova_venda = input("\nDeseja uma nova venda? (s/n): ").lower()

    if nova_venda != "s":
        break


# -------------------------
# RELATÓRIO FINAL
# -------------------------
print("\n============================")
print("RELATÓRIO FINAL DA LOJA")
print("============================")

print(f"Total de vendas: {len(vendas)}")
print(f"Faturamento total: R$ {total_faturado:.2f}")

if len(vendas) > 0:
    cliente_top = maior_compra(vendas)
    print(f"Cliente que mais comprou: {cliente_top['cliente']} (R$ {cliente_top['total']:.2f})")
    print(f"Média das vendas: R$ {calcular_media(vendas):.2f}")

print("\n=== RESUMO DAS VENDAS ===")
for v in vendas:
    print(f"Cliente: {v['cliente']} | Total: R$ {v['total']:.2f}")