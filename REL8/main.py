from database import Database
from player_database import PlayerDatabase

db = Database("bolt://34.237.136.96:7687", "neo4j", "coasts-heater-worm")
db.drop_all()

# Criando uma instância da classe PlayerDatabase
player_db = PlayerDatabase(db)

# Criando jogadores e partidas
player_db.create_player("Vinicius", 13)
player_db.create_player("John", 9)
player_db.create_player("Fefe", 20)
player_db.create_player("Beatriz", 28)
player_db.create_player("Julia", 12)

player_db.create_match(0, "0x1")
player_db.create_match(1, "2x1")
player_db.create_match(2, "4x4")
player_db.create_match(3, "1x5")
player_db.create_match(4, "3x2")

# Criando relação entre jogadores e partidas
player_db.insert_player_match(0, 13, "ganhou")
player_db.insert_player_match(0, 9, "ganhou")
player_db.insert_player_match(0, 20, "perdeu")
player_db.insert_player_match(0, 28, "perdeu")

player_db.insert_player_match(1, 13, "ganhou")
player_db.insert_player_match(1, 28, "ganhou")
player_db.insert_player_match(1, 20, "perdeu")
player_db.insert_player_match(1, 9, "perdeu")

player_db.insert_player_match(2, 28, "ganhou")
player_db.insert_player_match(2, 12, "ganhou")
player_db.insert_player_match(2, 13, "perdeu")
player_db.insert_player_match(2, 9, "??")

player_db.insert_player_match(3, 20, "ganhou")
player_db.insert_player_match(3, 13, "ganhou")
player_db.insert_player_match(3, 28, "perdeu")
player_db.insert_player_match(3, 9, "perdeu")

player_db.insert_player_match(4, 20, "ganhou")
player_db.insert_player_match(4, 28, "ganhou")
player_db.insert_player_match(4, 13, "perdeu")
player_db.insert_player_match(4, 9, "perdeu")

# deletando um jogador e uma partida
player_db.delete_player(12)
player_db.delete_match(0)

# atualizando um jogador, uma partida e uma pontuacao
player_db.update_player(13, "Vinnie")

player_db.update_match(2, "4x5")

player_db.update_player_match(9, 2, "perdeu")
# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(player_db.get_players())
print("Partidas:")
print(player_db.get_matches())

# Fechando a conexão com o banco de dados
db.close()