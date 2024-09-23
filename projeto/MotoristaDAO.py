from pymongo import MongoClient
from bson.objectid import ObjectId
from Classes import Corrida
from helper.writeAJson import writeAJson

class MotoristaDAO:

    def __init__(self, database):
        self.db = database

    def totalCorridas(self, id: str):

        result = self.database.collection.aggregate([
            {"$match": {"_id": id}},
            {"$unwind": "$corridas"},
            {"$count": "total"}
        ])

        writeAJson(result, "Total de corridas")

    def criar(self, corridas:Corrida, nota:int):
        
        try:
            res = self.db.collection.insert_one(
                {
                    "corridas": [vars(corrida) for corrida in corridas], 
                    "nota": nota
                }
            )
            print(f"Mortorista criado com a id: {res.inserted_id}")
            return res.inserted_id
        
        except Exception as e:
            print(f"Ocorreu um erro ao criar um motorista: {e}")
            return None

    def ler(self, id: str):

        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        
        except Exception as e:
            print(f"Ocorreu um erro ao procurar um motorista: {e}")
            return None

    def atualizar(self, id: str, corridas:Corrida, nota:int):

        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)}, 
                {
                    "$set": 
                    {
                    "corridas": [vars(corrida) for corrida in corridas], 
                    "nota": nota
                    }
                }
                )
            print(f"Dados do motorista atualizados: {res.modified_count} document(s) modified")
            return res.modified_count
        
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar od dados de um motorista: {e}")
            return None

    def deletar(self, id: str):
        
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        
        except Exception as e:
            print(f"Ocorreu um erro ao tentar deletar um motorista: {e}")
            return None