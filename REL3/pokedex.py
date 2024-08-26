from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database):
        self.database = database

    def busca_pokemon(self, nome):

        busca = self.database.collection.find({"name" : nome})

        return writeAJson(busca, f"{nome}:")
    
    def busca_tipo(self, nome):
        
