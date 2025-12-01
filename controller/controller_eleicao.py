import os
import dotenv
import pandas as pd

os.getenv("JSON_PATH_ELEITORES")

def finalizar_eleicao():
    print("Eleição finalizada com sucesso. Aperte qualquer tecla para exibir os resultados.")
    input("")

