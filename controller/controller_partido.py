import os
import json
from dotenv import load_dotenv
from models.partido import Partido
from utils.json_utils import salvar_db, input_info, carregar_db

load_dotenv()

db_partido = os.getenv("JSON_PATH_PARTIDO", "partidos.json")

def cadastrar_partido():
    nome = input_info("nome", "nome", db_partido, Partido)
    sigla = input("Digite a sigla: ")
    numero = input_info("numero", "numero", db_partido, Partido)
    partido = Partido(nome, sigla, numero)
    salvar_db(partido, db_partido, Partido)


def listar_partidos():
    print("\n--- Lista de Partidos ---")
    partidos = carregar_db(db_partido, Partido)
    if not partidos:
        print("Nenhum Partido cadastrado.")
        return
    for p in partidos:
        print(f"Nome: {p.nome_partido} - Sigla: {p.sigla} - Nº {p.numero_partido}")
    input("")

def apagar_partido():
    numero = input("Digite o número do partido a ser removido: ")
    partidos = carregar_db(db_partido, Partido)
    
    # Verifica se o número existe
    partido_encontrado = False
    novos_partidos = []
    for p in partidos:
        if p.numero_partido == numero:
            partido_encontrado = True
            continue
        novos_partidos.append(p)
    
    if not partido_encontrado:
        print("Número inválido, nenhum partido removido.")
        return

    # Salva novamente os dados
    dados = [p.to_dict() for p in novos_partidos]
    with open(db_partido, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    
    print(f"Partido com número {numero} removido com sucesso.")
