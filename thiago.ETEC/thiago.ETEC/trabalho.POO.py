class Cores:     
    VERMALHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    ROXO = '\033[35m'
    RESET = '\033[0m'
    
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
                nome = input(Cores.AMARELO + "Nome: " + Cores.RESET)
                if self.validar_nome(nome):
                    break
                print(Cores.VERMALHO + "Erro: Nome não pode ser vazio." + Cores.RESET)

            while True:
                idade = input(Cores.AMARELO + "Idade: " + Cores.RESET)
                if self.validar_idade(idade):
                    idade = int(idade)
                    break
                print(Cores.VERMALHO + "Erro: Idade deve ser numérica e maior que zero." + Cores.RESET)

            while True:
                email = input(Cores.AMARELO + "E-mail: " + Cores.RESET)
                if self.validar_email(email):
                    break
                print(Cores.VERMALHO + "Erro: E-mail inválido." + Cores.RESET)

            while True:
                telefone = input(Cores.AMARELO + "Telefone: " + Cores.RESET)
                if self.validar_telefone(telefone):
                    break
                print(Cores.VERMALHO + "Erro: Telefone deve conter apenas números e pelo menos 10 dígitos." + Cores.RESET)

            cliente = Cliente(nome, idade, email, telefone)

            self.clientes.append(cliente)
            self.salvar_todos_clientes()

            print(Cores.VERDE + "\nCliente cadastrado com sucesso!" + Cores.RESET)

        except Exception as erro:
            print(Cores.VERMALHO + f"Erro ao cadastrar cliente: {erro}" + Cores.RESET)

    # Listagem
    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("\nNenhum cliente cadastrado.")
            return

        print(Cores.AMARELO + "\n===== CLIENTES CADASTRADOS =====" + Cores.RESET)

        for indice, cliente in enumerate(self.clientes, start=1):
            print(Cores.VERDE + f"{indice} - {cliente}" + Cores.RESET)

    # Atualização
    def atualizar_cliente(self):
        if len(self.clientes) == 0:
            print(Cores.VERMALHO + "\nNenhum cliente cadastrado." + Cores.RESET)
            return

        self.listar_clientes()

        try:
            indice = int(
                input(Cores.VERDE + "\nDigite o número do cliente que deseja atualizar: " + Cores.RESET)
            ) - 1

            if indice < 0 or indice >= len(self.clientes):
                print("Cliente não encontrado.")
                return

            cliente = self.clientes[indice]

            print(Cores.VERDE + "\nPressione ENTER para manter o valor atual." + Cores.RESET)

            novo_nome = input(Cores.ROXO + f"Nome ({cliente.get_nome()}): " + Cores.RESET)

            nova_idade = input(Cores.ROXO + f"Idade ({cliente.get_idade()}): " + Cores.RESET)

            novo_email = input(Cores.ROXO + f"E-mail ({cliente.get_email()}): " + Cores.RESET)

            novo_telefone = input(Cores.ROXO + f"Telefone ({cliente.get_telefone()}): " + Cores.RESET)

            if novo_nome:
                if self.validar_nome(novo_nome):
                    cliente.set_nome(novo_nome)
                else:
                    print(Cores.VERMALHO + "Nome inválido. Mantido valor anterior." + Cores.RESET)

            if nova_idade:
                if self.validar_idade(nova_idade):
                    cliente.set_idade(int(nova_idade))
                else:
                    print(Cores.VERMALHO + "Idade inválida. Mantido valor anterior." + Cores.RESET)

            if novo_email:
                if self.validar_email(novo_email):
                    cliente.set_email(novo_email)
                else:
                    print(Cores.VERMALHO + "E-mail inválido. Mantido valor anterior." + Cores.RESET)

            if novo_telefone:
                if self.validar_telefone(novo_telefone):
                    cliente.set_telefone(novo_telefone)
                else:
                    print(Cores.VERMALHO + "Telefone inválido. Mantido valor anterior." + Cores.RESET)

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

            confirmacao = input(Cores.VERDE + f"Confirma a exclusão de {cliente.get_nome()}? (S/N): " + Cores.RESET).upper()

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
            print(Cores.VERMALHO + f"Erro ao salvar arquivo: {erro}" + Cores.RESET)

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
            print(Cores.VERMALHO + f"Erro ao carregar clientes: {erro}" + Cores.RESET)

    # Menu
    def executar(self):
        while True:
            print(Cores.AMARELO + "\n===== MENU PRINCIPAL =====" + Cores.RESET)
            print(Cores.AZUL + "1 - Cadastrar cliente" + Cores.RESET)
            print(Cores.AZUL + "2 - Listar clientes" + Cores.RESET)
            print(Cores.AZUL + "3 - Atualizar cliente" + Cores.RESET)
            print(Cores.AZUL + "4 - Excluir cliente" + Cores.RESET)
            print(Cores.AZUL + "5 - Sair" + Cores.RESET)

            opcao = input(Cores.VERDE + "Escolha uma opção: " + Cores.RESET)

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