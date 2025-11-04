import os
from dotenv import load_dotenv
from models.eleitor import Eleitor
from utils.json_utils import salvar_db, input_info, carregar_db, apagar_db

load_dotenv()

db_eleitores = os.getenv("JSON_PATH_ELEITORES")

def cadastrar_eleitor():
    nome = input_info("nome", "nome", db_eleitores, Eleitor)
    idade = input("digite sua idade: ")
    cpf = input_info("cpf", "cpf", db_eleitores, Eleitor)  
    eleitor = Eleitor(nome, idade, cpf)
    salvar_db(eleitor, db_eleitores, Eleitor)

def apagar_eleitor():
    cpf = input("Digite o cpf do eleitor a ser removido: ")
    apagar_db(cpf, db_eleitores, "eleitor", Eleitor)

def listar_eleitores():
    print("\n--- Lista de Eleitores ---")
    eleitores = carregar_db(db_eleitores, Eleitor)
    if not eleitores:
        print("Nenhum eleitor cadastrado.")
        return
    for c in eleitores:
        print(f"{c.nome} - {c.idade} anos - CPF: {c.cpf}")
    input("")
