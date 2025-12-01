import os
import json
from dotenv import load_dotenv
from models.partido import Partido
from utils.json_utils import salvar_db, carregar_db, verificar_input, apagar_db

load_dotenv()

db_partido = os.getenv("JSON_PATH_PARTIDO")

def listar_siglas_existentes():
    """Retorna uma string com todas as siglas ja cadastradas."""
    partidos = carregar_db(db_partido, Partido)
    lista = [p.sigla for p in partidos]
    return ", ".join(lista)

def cadastrar_partido():
    print("\n--- CADASTRO DE PARTIDO ---")
    
    # 1. NOME DO PARTIDO
    while True:
        nome = input("Digite o nome do partido: ").strip()
        
        if len(nome) < 3:
            print("Erro: O nome deve ter pelo menos 3 caracteres.")
            continue
            
        # Verifica se o nome ja existe (campo 'nome_partido' no JSON)
        if verificar_input(nome, "nome_partido", db_partido, Partido):
            print("Erro: Ja existe um partido cadastrado com este nome.")
        else:
            break

    # 2. SIGLA (Deve ser unica)
    while True:
        sigla = input("Digite a sigla do partido: ").strip().upper()
        
        if len(sigla) < 2:
            print("Erro: A sigla deve ter pelo menos 2 letras.")
            continue
            
        if verificar_input(sigla, "sigla", db_partido, Partido):
            print(f"Erro: A sigla '{sigla}' ja esta em uso.")
        else:
            break

    # 3. NUMERO DO PARTIDO (Deve ser unico)
    while True:
        numero = input("Digite o numero do partido: ").strip()
        
        if not numero.isdigit():
            print("Erro: O numero deve conter apenas digitos.")
            continue
            
        if verificar_input(numero, "numero_partido", db_partido, Partido):
            print(f"Erro: O numero '{numero}' ja pertence a outro partido.")
        else:
            break

    # Cria o objeto e salva
    novo_partido = Partido(nome, sigla, numero)
    salvar_db(novo_partido, db_partido, Partido)
    
    print(f"Sucesso: Partido '{nome}' ({sigla}) cadastrado.")

def listar_partidos():
    print("\n--- LISTA DE PARTIDOS ---")
    partidos = carregar_db(db_partido, Partido)
    
    if not partidos:
        print("Nenhum partido cadastrado.")
        return
        
    for p in partidos:
        # Ajuste os nomes dos atributos conforme sua classe Partido
        print(f"[{p.numero_partido}] {p.sigla} - {p.nome_partido}")
    
    input("\nPressione Enter para voltar...")

def apagar_partido():
    print("\n--- REMOVER PARTIDO ---")
    numero = input("Digite o numero do partido a ser removido: ")
    
    # Usa a funcao utilitaria para apagar pelo campo chave 'numero_partido'
    apagar_db(numero, db_partido, "numero_partido", Partido)