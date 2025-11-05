import json
import os

def carregar_db(arquivo,classe):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
            return [classe(**d) for d in dados]
        except json.JSONDecodeError:
            return []

def salvar_db(candidato, arquivo, classe):
    candidatos = carregar_db(arquivo, classe)
    candidatos.append(candidato)
    dados = [c.to_dict() for c in candidatos]
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def apagar_db(cpf, arquivo, cargo, classe):
    objeto = carregar_db(arquivo, classe)
    objetos = [c for c in objeto if c.cpf != cpf]

    if len(objetos) == len(objeto):
        print(f"Valor invalido, tente novamente.")
    else:
        dados = [o.to_dict() for o in objetos]
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)


def input_info(info, campo, db, classe):
    while True:
        valor = input(f"Digite seu {info}: ").strip()
        if not verificar_input(info, campo, db, classe):
            return valor
        print(f"{campo} '{info}' já cadastrado. Tente outro.")

def verificar_input(info, campo, db, classe):
    candidatos = carregar_db(db, classe)  
    
    for c in candidatos:
        dados = c.to_dict()
        if dados.get(campo) == info:
            print(f"Erro: {info} já cadastrado no campo '{campo}'.")
            return True
    return False
