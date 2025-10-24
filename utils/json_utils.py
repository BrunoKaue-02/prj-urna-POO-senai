import json
import os
from models.candidato import Candidato

def carregar_db(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
            return [Candidato(**d) for d in dados]
        except json.JSONDecodeError:
            return []


def salvar_db(candidato, arquivo):
    candidatos = carregar_db(arquivo)
    candidatos.append(candidato)
    dados = [c.to_dict() for c in candidatos]
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f" Candidato '{candidato.nome}' adicionado com sucesso.")


def apagar_candidato(numero, arquivo):
    candidatos = carregar_db(arquivo)
    novos_candidatos = [c for c in candidatos if c.numero != numero]

    if len(novos_candidatos) == len(candidatos):
        print(f"Nenhum candidato encontrado com número {numero}.")
    else:
        dados = [c.to_dict() for c in novos_candidatos]
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Candidato com número {numero} removido com sucesso.")

def listar():
    print("\n--- Lista de Candidatos ---")
    candidatos = carregar_db()
    if not candidatos:
        print("Nenhum candidato cadastrado.")
        return
    for c in candidatos:
        print(f"{c.nome} - {c.idade} anos - CPF: {c.cpf} - Partido: {c.partido} - Nº {c.numero}")

def input_info(info, campo, db):
    while True:
        valor = input(f"Digite seu {info}: ").strip()
        if not verificar_input(valor, campo, db):
            return valor
        print(f"{campo} '{valor}' já cadastrado. Tente outro.")

def verificar_input(info, campo, db):
    candidatos = carregar_db(db)  
    
    for c in candidatos:
        dados = c.to_dict()
        if dados.get(campo) == info:
            print(f"Erro: {info} já cadastrado no campo '{campo}'.")
            return True
    return False
