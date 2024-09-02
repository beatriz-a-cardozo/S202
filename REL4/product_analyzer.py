from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database):
        self.database = database

    def totalVendas(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"data": "$data_compra"}, "total": {"$sum": "$produtos.quantidade"}}},
            {"$group": {"_id": "$_id.data", "total": {"$sum": "$total"}}},
            {"$sort": {"_id": 1}}
        ])

        writeAJson(result, "Quantidade total de vendas por dia")

    def produtoMais(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido em todas as compras")

    def clienteRico(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "Cliente que mais gastou em uma unica compra")

    def produtoMais1(self):
        result = self.database.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total" : {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total": {"$gt": 1}}}
        ])

        writeAJson(result, "Produto que vendeu mais de um item")