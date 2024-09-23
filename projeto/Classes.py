class Passageiro:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota, distancia, valor, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, corridas, nota):
        if corridas is None:
            corridas = []
        self.corridas = corridas
        self.nota = nota
