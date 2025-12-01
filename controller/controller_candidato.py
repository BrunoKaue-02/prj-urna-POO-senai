import os
from dotenv import load_dotenv
from models.candidato import Candidato
from models.partido import Partido
from utils.json_utils import salvar_db, apagar_db, carregar_db, verificar_input

load_dotenv()

db_candidatos = os.getenv("JSON_PATH_CANDIDATOS")
db_partidos = os.getenv("JSON_PATH_PARTIDO")

def verificar_partido_existente(sigla_digitada):
    """
    Verifica se a sigla existe no arquivo de partidos carregado.
    Retorna True se encontrar, False se nao encontrar.
    """
    partidos = carregar_db(db_partidos, Partido)
    
    for p in partidos:
        # Compara a sigla do objeto (em maiusculo para evitar erros de digitacao)
        if p.sigla.upper() == sigla_digitada.upper():
            return True
            
    return False

def listar_siglas_disponiveis():
    """Funcao auxiliar para listar siglas para o usuario ver"""
    partidos = carregar_db(db_partidos, Partido)
    lista = [p.sigla for p in partidos]
    return ", ".join(lista)

def cadastrar_candidato():
    print("\n--- CADASTRO DE CANDIDATO ---")

    # 1. NOME (Campo nao unico - Pode haver homonimos)
    while True:
        nome = input("Digite o nome do candidato: ").strip()
        if len(nome) >= 3:
            break
        print("Erro: Nome invalido. O nome deve ter pelo menos 3 caracteres.")

    # 2. IDADE (Campo nao unico)
    while True:
        try:
            idade_input = input("Digite a idade: ").strip()
            idade = int(idade_input)
            if idade >= 18:
                break
            print("Erro: O candidato deve ter pelo menos 18 anos.")
        except ValueError:
            print("Erro: Idade invalida. Insira apenas numeros inteiros.")

    # 3. CPF (Campo UNICO - Nao pode repetir)
    while True:
        cpf = input("Digite o CPF (apenas numeros): ").strip()
        if len(cpf) != 11 or not cpf.isdigit():
            print("Erro: CPF invalido. Deve conter exatamente 11 digitos numericos.")
            continue
            
        # Verifica se ja existe no JSON
        if verificar_input(cpf, "cpf", db_candidatos, Candidato):
            print("Erro: CPF ja cadastrado no sistema. Tente outro.")
        else:
            break  

    # 4. PARTIDO (Deve existir no cadastro de partidos)
    while True:
        print(f"Partidos disponiveis: {listar_siglas_disponiveis()}")
        sigla_partido = input("Digite a sigla do partido: ").strip().upper()
        
        if sigla_partido == "":
            print("Erro: A sigla nao pode ser vazia.")
            continue

        if verificar_partido_existente(sigla_partido):
            break
        else:
            print("Erro: Partido nao encontrado. Verifique a sigla ou cadastre o partido antes.")

    # 5. NUMERO (Campo UNICO - Dois candidatos nao podem ter o mesmo numero)
    while True:    
        numero = input("Digite o numero do candidato (2 digitos): ").strip()
        
        if not numero.isdigit() or len(numero) != 2:
            print("Erro: Numero invalido. Deve conter exatamente 2 digitos.")
            continue
            
        if verificar_input(numero, "numero", db_candidatos, Candidato):
            print("Erro: Este numero ja pertence a outro candidato.")
        else:
            break

    # 6. CARGO (Campo nao unico)
    while True:
        cargo = input("Digite o cargo (ex: Prefeito, Vereador): ").strip()
        if len(cargo) > 2:
            break
        print("Erro: Cargo invalido.")

    # Criacao do objeto (incluindo votos=0 para iniciar a contagem)
    novo_candidato = Candidato(nome, idade, cpf, sigla_partido, numero, cargo, votos=0)
    
    salvar_db(novo_candidato, db_candidatos, Candidato)
    print("Sucesso: Candidato cadastrado.")

def apagar_candidato():
    print("\n--- REMOVER CANDIDATO ---")
    numero = input("Digite o numero do candidato a ser removido: ")
    
    # Chama a funcao de apagar passando o campo chave "numero"
    apagar_db(numero, db_candidatos, "numero", Candidato)

def listar_candidatos():
    print("\n--- LISTA DE CANDIDATOS ---")
    candidatos = carregar_db(db_candidatos, Candidato)
    
    if not candidatos:
        print("Nenhum candidato cadastrado.")
    else:
        for c in candidatos:
            # Exibe de forma organizada
            print(f"[{c.numero}] {c.nome} ({c.partido}) - {c.cargo} | Votos: {c.votos}")
            
    input("\nPressione Enter para voltar...")