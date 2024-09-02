from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

product = ProductAnalyzer(db)

product.totalVendas # cria o arquivo json que mostra o total de vendas por dia
product.produtoMais # cria o arquivo json do produto mais vendido em todas as compras
product.clienteRico # cria o arquivo json do cliente que mais gastou numa unica compra
product.produtoMais1 # cria o arquivo json dos produtos que venderam mais de um item