while True:
    print("--- SISTEMA DE VENDAS ---")

    nome_cliente = input("Digite o nome do cliente: ")

    total_compra = 0

    qtd_produtos = int(input("Quantos produtos serão comprados? "))

    for i in range(qtd_produtos):
        print(f"Produto {i+1}")

        nome_produto = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade: "))

        subtotal = preco * quantidade
        total_compra += subtotal

        print(f"Subtotal: R$ {subtotal:.2f}")


    if total_compra >= 500:
        desconto = total_compra * 0.10
    elif total_compra >= 200 and total_compra < 500:
        desconto = total_compra * 0.05
    else:
        desconto = 0

    total_final = total_compra - desconto

    print("--- RESUMO ---")
    print(f"Cliente: {nome_cliente}")
    print(f"Total da compra: R$ {total_compra:.2f}")
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Total final: R$ {total_final:.2f}")

    continuar = input("Deseja realizar nova venda? (S/N): ").upper()

    if continuar == "N":
        print("Encerrando sistema...")
        break