class PlayerDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name, player_id): # criando um jogador
        query = "CREATE (:Player {name: $name, player_id: $player_id})"
        parameters = {"name": name, "player_id": player_id}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id, resultado): # criando uma partida
        query = "CREATE (:Match {match_id: $match_id, resultado: $resultado})"
        parameters = {"match_id": match_id, "resultado": resultado}
        self.db.execute_query(query, parameters)

    def insert_player_match(self, match_id, player_id, ganhador): # relacionando um jogador a uma partida com a ganhador individual de cada jogador
        query = "MATCH (p:Player {player_id: $player_id}), (m:Match {match_id: $match_id}) CREATE (p)-[:PARTICIPA {ganhador: $ganhador}]->(m)"
        parameters = {"player_id": player_id, "match_id": match_id, "ganhador": ganhador}
        self.db.execute_query(query, parameters)

    def get_players(self): # lista de jogadores
        query = "MATCH (p:Player) RETURN p.name AS name, p.player_id AS id"
        results = self.db.execute_query(query)
        return [{"name": result["name"], "id": result["id"]} for result in results]

    def get_matches(self): # lista de partidas
        query = "MATCH (m:Match) RETURN m.resultado AS resultado, m.match_id AS id"
        results = self.db.execute_query(query)
        return [{"resultado": result["resultado"], "id": result["id"]} for result in results]

    def update_player(self, player_id, new_name): # edita o nome do jogador
        query = "MATCH (p:Player {player_id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_match(self, match_id, new_result): # edita o resultado da partida
        query = "MATCH (m:Match {match_id: $match_id}) SET m.resultado = $new_result"
        parameters = {"match_id": match_id, "new_result": new_result}
        self.db.execute_query(query, parameters)

    def update_player_match(self, player_id, match_id, new_ganhador): # atualiza a pontuação individual
        query = "MATCH (p:Player {player_id: $player_id})-[r:PARTICIPA]->(m:Match {match_id: $match_id})SET r.ganhador = $new_ganhador"
        parameters =  {"player_id": player_id, "match_id": match_id, "new_ganhador": new_ganhador}
        self.db.execute_query(query,parameters)

    def delete_player(self, player_id): #deleta o jogador
        query = "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id): # deleta a partida
        query = "MATCH (m:Match {match_id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)
        