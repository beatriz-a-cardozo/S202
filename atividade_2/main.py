from database import Database
from query import  TeachersDatabase
from teacher_crud import TeacherCRUD
from cli import TeacherCLI


db = Database("bolt://3.88.195.221:7687", "neo4j", "signature-lockers-spring")
#db.drop_all()
# funcoes para questao 1 e 2, dando run mostrara os reultados identados
queries = TeachersDatabase(db)
crud = TeacherCRUD(db)

queries.search_teacher_renzo()
queries.search_teachers_startsWithM()
queries.search_allCities()
queries.search_schools_byNumber()
queries.search_maisJovem_maisVelho()
queries.average_population()
queries.search_city_byCEP()
queries.teacher_terceiroCaracter()

print("-------------------------------------------------- Questao 3")
print("--------------------------------------- letra b")
crud.create('Chris Lima', 1956, '189.052.396-66')
print()
print("--------------------------------------- letra c")
crud.read('Chris Lima')
print()
print("--------------------------------------- letra d")
crud.update('Chris Lima', '162.052.777-77')

#para evitar criar de novo
#crud.delete('Chris Lima')

print("--------------------------------------- letra e")
cli = TeacherCLI(crud)
cli.run()