from teacher_crud import TeacherCRUD

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


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("delete", self.delete_teacher)
        self.add_command("update", self.update_teacher)

    def create_teacher(self):
        name = input("Insira o nome do professor: ")
        ano_nasc = input("Insira o ano de nascimento do professor: ")
        cpf = input("Insira o CPF do professor: ")
        self.teacher_crud.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Insira o nome do professor para leitura: ")
        self.teacher_crud.read(name)

    def delete_teacher(self):
        name = input("Insira o nome do professor para deletar: ")
        self.teacher_crud.delete(name)

    def update_teacher(self):
        name = input("Insira o nome do professor para atualizar: ")
        new_cpf = input("Insira o novo CPF do professor: ")
        self.teacher_crud.update(name, new_cpf)
        
    def run(self):
        print("Bem-Vindo ao TeacherCLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()