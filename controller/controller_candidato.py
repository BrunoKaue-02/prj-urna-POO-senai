import os
from dotenv import load_dotenv
from models.candidato import Candidato
from utils.json_utils import salvar_db, input_info, apagar_db, carregar_db

load_dotenv()

db_candidatos = os.getenv("JSON_PATH_CANDIDATOS")

def cadastrar_candidato():
    nome = input_info("nome", "nome", db_candidatos, Candidato)
    idade = input("Digite sua idade: ")
    cpf = input_info("cpf", "cpf", db_candidatos, Candidato)  
    partido = input("Digite seu partido: ")
    numero = input_info("numero", "numero", db_candidatos, Candidato) 
    cargo = input_info("cargo", "cargo", db_candidatos, Candidato)
    c = Candidato(nome, idade, cpf, partido, numero, cargo)
    salvar_db(c, db_candidatos, Candidato)

def apagar_candidato():
    numero = input("Digite o número do candidato a ser removido: ")
    apagar_db(numero, db_candidatos, "candidato", Candidato)

def listar_candidatos():
    print("\n--- Lista de Candidatos ---")
    candidatos = carregar_db(db_candidatos, Candidato)
    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return
    for c in candidatos:
        print(f"{c.nome} - {c.idade} anos - CPF: {c.cpf} - Partido: {c.partido} - Nº {c.numero} - {c.cargo}")
    input("")

