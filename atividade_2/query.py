class TeachersDatabase:

    def __init__(self, database):
        self.db = database
    
    def search_teacher_renzo(self):
    
        query = "MATCH (t:Teacher {name:'Renzo'}) RETURN t.cpf AS cpf, t.ano_nasc AS ano_nasc"
    
        result = self.db.execute_query(query)

        print("-------------------------------------------------- Questao 1")
        print("--------------------------------------- letra a")
        for teacher in result:
            print()
            print("{")
            print(f"    cpf: {teacher['cpf']}")
            print(f"    ano de nascimento: {teacher['ano_nasc']}")
            print("}")
            
        print()

    def search_teachers_startsWithM(self):

        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"

        result = self.db.execute_query(query)

        print("--------------------------------------- letra b")
        for teacher in result:
            print()
            print("{")
            print(f"    nome: {teacher['name']}")
            print(f"    cpf: {teacher['cpf']}")
            print("}")
            
        print()

    def search_allCities(self):

        query = "MATCH (c:City) RETURN c.name AS city_name"

        result = self.db.execute_query(query) 

        print("--------------------------------------- letra c")
        for city in result:
            print()
            print("{")
            print(f"    nome da cidade: {city['city_name']}")
            print("}")
            
        print()

    def search_schools_byNumber(self):

        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS school_name, s.address AS address, s.number AS number"

        result = self.db.execute_query(query)

        print("--------------------------------------- letra d")
        for school in result:
            print()
            print("{")
            print(f"    nome da escola: {school['school_name']}")
            print(f"    endereço: {school['address']}")
            print(f"    numero: {school['number']}")
            print("}")

        print()
    
    def search_maisJovem_maisVelho(self):

        query1 = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS mais_jovem"
        query2 = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS mais_velho"

        result1 = self.db.execute_query(query1)
        result2 = self.db.execute_query(query2)

        print("-------------------------------------------------- Questao 2")
        print("--------------------------------------- letra a")
        print()
        print(f"Ano de nascimento do professor mais jovem:  {result1[0]['mais_jovem']}")
        print()
        
        print(f"Ano de nascimento do professor mais velho: {result2[0]['mais_velho']}")
        
        print()

    def average_population(self):

        query = "MATCH (c:City) RETURN  CEIL(AVG(c.population)) AS media"

        result = self.db.execute_query(query)

        print("--------------------------------------- letra b")
        print()
        print(f"media aritmetica da populacao: {result[0]['media']}")
        print()

    def search_city_byCEP(self):

        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') AS new_name"

        result = self.db.execute_query(query)

        print("--------------------------------------- letra c")
        print()
        print(f"nome da cidade: {result[0]['new_name']}")
        print()

    def teacher_terceiroCaracter(self):

        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS terceiro_caracter"

        result = self.db.execute_query(query)

        print("--------------------------------------- letra d")
        for teachers in result:
            print()
            print(f"Terceiro caracter do nome do professor: {teachers['terceiro_caracter']}")

        print()
