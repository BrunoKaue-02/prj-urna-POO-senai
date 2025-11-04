import os
from dotenv import load_dotenv
from models.candidato import Candidato
from utils.json_utils import salvar_db, input_info, apagar_db

load_dotenv()

db_candidatos = os.getenv("JSON_PATH_CANDIDATOS", "canditados.json")

def cadastrar_candidato():
    nome = input_info("nome", "nome", db_candidatos)
    idade = input("digite sua idade: ")
    cpf = input_info("cpf", "cpf", db_candidatos)  
    partido = input("Digite seu partido: ")
    numero = input_info("numero", "numero", db_candidatos) 
    c = Candidato(nome, idade, cpf, partido, numero)
    salvar_db(c, db_candidatos)

def apagar_candidato():
    numero = input_info("numero", "numero", db_candidatos)
    apagar_db(numero, db_candidatos, "candidato")

