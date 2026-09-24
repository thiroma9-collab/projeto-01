class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__email = email
        self.__telefone = telefone

    # Getters
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_email(self):
        return self.__email

    def get_telefone(self):
        return self.__telefone

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def set_email(self, email):
        self.__email = email

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return (
            f"Nome: {self.__nome} | "
            f"Idade: {self.__idade} | "
            f"E-mail: {self.__email} | "
            f"Telefone: {self.__telefone}"
        )


class SistemaCadastro:
    def __init__(self):
        self.clientes = []
        self.carregar_clientes()

    # Validações
    # 
    def validar_nome(self, nome):
        return nome.strip() != ""

    def validar_idade(self, idade):
        return idade.isdigit() and int(idade) > 0

    def validar_email(self, email):
        return "@" in email and "." in email

    def validar_telefone(self, telefone):
        return telefone.isdigit() and len(telefone) >= 10

    # Cadastro
    def cadastrar_cliente(self):
        try:
            while True:
                nome = input("Nome: ")
                if self.validar_nome(nome):
                    break
                print("Erro: Nome não pode ser vazio.")

            while True:
                idade = input("Idade: ")
                if self.validar_idade(idade):
                    idade = int(idade)
                    break
                print("Erro: Idade deve ser numérica e maior que zero.")

            while True:
                email = input("E-mail: ")
                if self.validar_email(email):
                    break
                print("Erro: E-mail inválido.")

            while True:
                telefone = input("Telefone: ")
                if self.validar_telefone(telefone):
                    break
                print(
                    "Erro: Telefone deve conter apenas números e pelo menos 10 dígitos."
                )

            cliente = Cliente(nome, idade, email, telefone)

            self.clientes.append(cliente)
            self.salvar_todos_clientes()

            print("\nCliente cadastrado com sucesso!")

        except Exception as erro:
            print(f"Erro ao cadastrar cliente: {erro}")

    # Listagem
    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("\nNenhum cliente cadastrado.")
            return

        print("\n===== CLIENTES CADASTRADOS =====")

        for indice, cliente in enumerate(self.clientes, start=1):
            print(f"{indice} - {cliente}")

    # Atualização
    def atualizar_cliente(self):
        if len(self.clientes) == 0:
            print("\nNenhum cliente cadastrado.")
            return

        self.listar_clientes()

        try:
            indice = int(
                input("\nDigite o número do cliente que deseja atualizar: ")
            ) - 1

            if indice < 0 or indice >= len(self.clientes):
                print("Cliente não encontrado.")
                return

            cliente = self.clientes[indice]

            print("\nPressione ENTER para manter o valor atual.")

            novo_nome = input(
                f"Nome ({cliente.get_nome()}): "
            )

            nova_idade = input(
                f"Idade ({cliente.get_idade()}): "
            )

            novo_email = input(
                f"E-mail ({cliente.get_email()}): "
            )

            novo_telefone = input(
                f"Telefone ({cliente.get_telefone()}): "
            )

            if novo_nome:
                if self.validar_nome(novo_nome):
                    cliente.set_nome(novo_nome)
                else:
                    print("Nome inválido. Mantido valor anterior.")

            if nova_idade:
                if self.validar_idade(nova_idade):
                    cliente.set_idade(int(nova_idade))
                else:
                    print("Idade inválida. Mantido valor anterior.")

            if novo_email:
                if self.validar_email(novo_email):
                    cliente.set_email(novo_email)
                else:
                    print("E-mail inválido. Mantido valor anterior.")

            if novo_telefone:
                if self.validar_telefone(novo_telefone):
                    cliente.set_telefone(novo_telefone)
                else:
                    print("Telefone inválido. Mantido valor anterior.")

            self.salvar_todos_clientes()

            print("\nCliente atualizado com sucesso!")

        except ValueError:
            print("Digite um número válido.")

    # Exclusão
    def excluir_cliente(self):
        if len(self.clientes) == 0:
            print("\nNenhum cliente cadastrado.")
            return

        self.listar_clientes()

        try:
            indice = int(
                input("\nDigite o número do cliente que deseja excluir: ")
            ) - 1

            if indice < 0 or indice >= len(self.clientes):
                print("Cliente não encontrado.")
                return

            cliente = self.clientes[indice]

            confirmacao = input(
                f"Confirma a exclusão de {cliente.get_nome()}? (S/N): "
            ).upper()

            if confirmacao == "S":
                self.clientes.pop(indice)
                self.salvar_todos_clientes()
                print("Cliente excluído com sucesso!")
            else:
                print("Exclusão cancelada.")

        except ValueError:
            print("Digite um número válido.")

    # Arquivos
    def salvar_todos_clientes(self):
        try:
            with open("clientes.txt", "w", encoding="utf-8") as arquivo:
                for cliente in self.clientes:
                    arquivo.write(
                        f"{cliente.get_nome()};"
                        f"{cliente.get_idade()};"
                        f"{cliente.get_email()};"
                        f"{cliente.get_telefone()}\n"
                    )
        except Exception as erro:
            print(f"Erro ao salvar arquivo: {erro}")

    def carregar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")

                    if len(dados) == 4:
                        nome, idade, email, telefone = dados

                        cliente = Cliente(
                            nome,
                            int(idade),
                            email,
                            telefone
                        )

                        self.clientes.append(cliente)

        except FileNotFoundError:
            pass
        except Exception as erro:
            print(f"Erro ao carregar clientes: {erro}")

    # Menu
    def executar(self):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Atualizar cliente")
            print("4 - Excluir cliente")
            print("5 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_cliente()

            elif opcao == "2":
                self.listar_clientes()

            elif opcao == "3":
                self.atualizar_cliente()

            elif opcao == "4":
                self.excluir_cliente()

            elif opcao == "5":
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida. Tente novamente.")


# Programa principal
sistema = SistemaCadastro()
sistema.executar()