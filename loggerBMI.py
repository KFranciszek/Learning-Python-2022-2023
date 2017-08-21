# Usługa do zapisywania logów działania oraz błędów do pliku. 

#logowanie wywołania usługi dicBMI
import logging
import dicBMI
from dicBMI import team

formatLogging = '[%(asctime).20s] [%(levelname)s] %(message)s'
logging.basicConfig(filename='D:\Python\Projekt\python1.log',
                    level=logging.DEBUG,
                    format=formatLogging)
logger=logging.getLogger()
logger.info(dicBMI)
logger.info(team)

