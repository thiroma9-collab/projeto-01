while True:
    cliente = input("digite o nome do cliente: ")
    produtos = int(input("quantos produtos serão comprados: "))

    total = 0

    for i in range(quantidades_produtos):
        print(f"n = produto {i + 1}")
        nome_produto = input("nome do protudo: ")
        preco = float(input("preco do produto: "))
        quantidade = int(input("quantidade: "))

        subtotal = preco * quantidade
        total = subtotal
        print(f"subtotal de {nome_produto}: $ {subtotal: f}")
    if total >500:
        desconto = total * 10