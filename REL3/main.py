from database import Database
#from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

pokedex = Pokedex(db)

entrada = input("Digite o nome do Pokemon que deseja procurar: ")

pokedex.busca_pokemon(entrada)


