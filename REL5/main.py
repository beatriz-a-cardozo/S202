from database import Database
from helper.writeAJson import writeAJson
from livrosModel import LivrosModel
from cli import LivrosCLI

db = Database(database="relatorio_05", collection="livros")
LivrosModel = LivrosModel(database=db)


livrosCLI = LivrosCLI(LivrosModel)
livrosCLI.run()