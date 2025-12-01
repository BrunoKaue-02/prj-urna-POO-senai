import os
from dotenv import load_dotenv
from models.eleitor import Eleitor
from utils.json_utils import salvar_db, input_info, carregar_db, apagar_db

load_dotenv()

db_eleitores = os.getenv("JSON_PATH_ELEITORES")

def cadastrar_eleitor():
    while True:
        
        nome = input_info("nome", "nome", db_eleitores, Eleitor)
        if nome == "" or len(nome) < 3:
            print("Nome inválido. O nome deve ter pelo menos 3 caracteres.")
        else:
            break
    
    while True:
        try:
            idade = int(input("digite sua idade: "))
            if idade < 18:
                print("Idade inválida. Eleitor deve ser maior de 18 anos.")
            else:
                break
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro.")
    while True:
        cpf = input_info("cpf", "cpf", db_eleitores, Eleitor)  
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
        else:
            break  
        ##implementar validação do CPF existente no banco de dados
    
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
