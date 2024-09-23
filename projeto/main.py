from database import Database
from helper.writeAJson import writeAJson
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="projeto1", collection="motoristas")
db.resetDatabase()

MotoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(MotoristaDAO)
motoristaCLI.run()