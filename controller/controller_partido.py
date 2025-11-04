import os
from dotenv import load_dotenv
from models.partido import Partido
from utils.json_utils import salvar_db, input_info, apagar_db, carregar_db

load_dotenv()

db_partido = os.getenv("JSON_PATH_PARTIDO")

def cadastrar_partido():
    nome = input_info("nome", "nome", db_partido, Partido)
    sigla = input("Digite sua sigla: ")
    numero = input_info("numero", "numero", db_partido, Partido)  
    partido = Partido(nome, sigla, numero)
    salvar_db(partido, db_partido, Partido)