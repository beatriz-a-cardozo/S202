# --------------------------------------------- CLASSE PROFESSOR ---------------------------------------------
class Professor(): #criando uma classe em python
    def __init__(self, nome): # o metodo '__init__' eh o construtor, 
        self.nome = nome      # responsavel por inicializar as variaveis de instancia de uma classe
        
# criando os outros metodos pedidos:
    def ministar_aula(self, assunto): 
        print(f'O professor {self.nome} esta ministrando uma aula sobre {assunto}') 

# ----------------------------------------------- CLASSE ALUNO -----------------------------------------------
class Aluno():
    def __init__(self, nome):
        self.nome = nome # 'self' funciona como um this

    def presenca(self):
        print(f'O aluno {self.nome} esta presente.')

# ---------------------------------------------- CLASSE AULA ----------------------------------------------
class Aula():
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print(f'Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        for aluno in self.alunos:
            aluno.presenca()


professor = Professor("Lucas")
# teste -> professor.ministar_aula("S202")

aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
# teste -> aluno1.presenca()

aula = Aula(professor, "Programacao Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

# -> interacao para treinar python
seuNome = Aluno(input("Assine a lista: "))
aula.adicionar_aluno(seuNome)

aula.listar_presenca()

