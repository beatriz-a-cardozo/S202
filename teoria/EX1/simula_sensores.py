import threading # lib para se trabalhar com threads
import time # permite executar uma Thread mais devagar
from pymongo import MongoClient
import json
import random

# -----------------------------------------------------------------------------------> setando o banco de dados
client = MongoClient('mongodb://localhost:27017') # abrindo e guardando uma conexão com o MongoDB server

db = client['bancoiot'] # criando o acesso ao Banco de Dados: bancoiot

sensores = db.sensores # criando acesso a uma coleção

with open('teoria/EX1/json/dataset.json', 'r') as f:
    data = json.load(f)

result = db.sensores.insert_many(data) # inserindo um documento com algumas instâncias
                                                        # de exemplo já criadas
# verificando se a inserção deu certo
if result.acknowledged:
    print('Documento adcionado!')
else:
    print('Erro ao inserir documento!')

# -----------------------------------------------------------------------------------------------------> thread
def tempSensor(nome, intervalo):
    while True:
        doc = sensores.find_one({"nomeSensor" : nome}) # busca o documento do sensor no banco de dados

        if doc["sensorAlarmado"]: # caso o sensor já estiver alarmado
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {nome}")
            break # não gera mais valores

        else:
            temp = random.uniform(30, 40) # gera uma temperatura aleatória
            temp = round(temp, 0)
        
            # atualizando o documento
            sensores.update_one({"nomeSensor" : nome}, {"$set" : {"valorSensor" : temp}})
            
            print(f"{nome} : {temp}")

            if temp > 38: # verifica a temperatura
                # atualiza o status do sensor
                sensores.update_one({"nomeSensor" : nome}, {"$set" : {"sensorAlarmado" : True}})

        time.sleep(intervalo) # espera {intervalo} segundos 

# -----------------------------------------------------------------------------> criando e iniciando as threads
thread1 = threading.Thread(target=tempSensor, args=("Temp1", 2))
thread2 = threading.Thread(target=tempSensor, args=("Temp2", 4))
thread3 = threading.Thread(target=tempSensor, args=("Temp3", 6))
thread4 = threading.Thread(target=tempSensor, args=("Temp4", 8))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
