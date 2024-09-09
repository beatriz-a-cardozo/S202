class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Insira um comando: ")
            if command == "quit":
                print("Tchau!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido. Tente de novo.")


class LivrosCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        titulo = input("Entre com o titulo do livro: ")
        autor = input("Entre com o nome do autor: ")
        ano = int(input("Entre com o ano de publicacao: "))
        preco = float(input("Entre com o preco do livro: "))
        self.livro_model.create_livro(titulo, autor, ano, preco)

    def read_livro(self):
        id = input("Insira a id: ")
        livro = self.livro_model.read_livro_by_id(id)
        if livro:
            print(f"titulo: {livro['titulo']}")
            print(f"autor: {livro['autor']}")
            print(f"ano: {livro['ano']}")
            print(f"preco: {livro['preco']}")

    def update_livro(self):
        id = input("Insira a id: ")
        titulo = input("Insira o novo titulo: ")
        autor = input("Insira o novo nome do autor: ")
        ano = int(input("Insira o novo ano de publicacao: "))
        preco = float(input("Insira o novo preco do livro: "))
        self.livro_model.update_livro(id, titulo, autor, ano, preco)

    def delete_livro(self):
        id = input("insira a id do livro que deseja excluir: ")
        self.livro_model.delete_livro(id)
        
    def run(self):
        print("Bem-Vindo ao Livro CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()
        