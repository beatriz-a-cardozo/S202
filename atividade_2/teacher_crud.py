class TeacherCRUD:

    def __init__(self, database):
        
        self.db = database

    def create(self, name, ano_nasc, cpf): # cria um teacher

        query = "CREATE (:Teacher{name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"

        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}

        self.db.execute_query(query, parameters)

        print(f"Teacher {name} criado com sucesso!")

    def read(self, name): # retorna apenas um teacher

        query = "MATCH (t:Teacher {name: $name}) RETURN t"

        parameters = {"name": name}

        result = self.db.execute_query(query, parameters)
        teacher = result[0]['t']

        print()
        print("{")
        print(f"    nome: {teacher['name']}")
        print(f"    ano de nascimento: {teacher['ano_nasc']}")
        print(f"    cpf: {teacher['cpf']}")
        print("}")
        print()

    def delete(self, name): #deleta teacher com base no nome

        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"

        parameters = {"name": name}

        self.db.execute_query(query, parameters)

        print(f"Teacher {name} deletado com sucesso!")

    def update(self, name, newCpf): # atualiza o cpf com base no nome
        
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"

        parameters = {"name": name, "newCpf": newCpf}

        self.db.execute_query(query, parameters)

        print(f"cpf do Teacher {name} atualizado com sucesso!")

