from Classes import Passageiro
from Classes import Corrida

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


class MotoristaCLI(SimpleCLI):

    def __init__(self, motorista_model):

        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.criar_motorista)
        self.add_command("read", self.ler_motorista)
        self.add_command("update", self.atualizar_motorista)
        self.add_command("delete", self.deletar_motorista)

    def criar_motorista(self):

        aux = 0

        print("Criar motorista")

        corridas = []
        while aux == 0:

            nota = input("Nota da corrida: ")
            distancia = input("Distancia da corrida: ")
            valor = input("Valor da corrida: ")
            nome = input("Nome do passageiro: ")
            documento = input("Documento do passageiro: ")

            passageiro = Passageiro(nome, documento)

            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

            aux = input("Deseja adicionar mais uma corrida?")
        
        nota = 2

        self.motorista_model.criar(corridas, nota)

    def ler_motorista(self):

        id = input("Insira a id: ")

        motorista = self.motorista_model.ler(id)

        if motorista:
            print(f"corridas: {motorista['corridas']}")
            print(f"nota: {motorista['nota']}")
            

    def atualizar_motorista(self):

        id = input("Insira a id: ")

        aux = 0

        print("Criar motorista")

        corridas = []
        while aux == 0:

            nota = input("Insira a nova nota da corrida: ")
            distancia = input("Insira a nova distancia da corrida: ")
            valor = input("Insira o novo valor da corrida: ")
            nome = input("Insira o novo nome do passageiro: ")
            documento = input("Insira o novo documento do passageiro: ")

            passageiro = Passageiro(nome, documento)

            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)

            aux = input("Deseja adicionar mais uma corrida?")
        
        nota = int(input("Insira a nova nota: "))
        
        self.motorista_model.atualizar(id, corridas, nota)

    def deletar_motorista(self):
        id = input("insira a id do motorista que deseja excluir: ")
        self.motorista_model.deletar(id)
        
    def run(self):
        print("Bem-Vindo ao motorista CLI!")
        print("Comandos disponiveis: create, read, update, delete, quit")
        super().run()