import os
import json
from dotenv import load_dotenv

# Importando os Models e Utils do seu projeto
from models.eleitor import Eleitor
from models.candidato import Candidato
from utils.json_utils import carregar_db

# Carrega variáveis de ambiente
load_dotenv()

DB_ELEITORES = os.getenv("JSON_PATH_ELEITORES")
DB_CANDIDATOS = os.getenv("JSON_PATH_CANDIDATOS")

def buscar_candidato_info(numero):
    """
    Busca apenas os dados do candidato para mostrar na tela (sem salvar nada ainda).
    Retorna o objeto Candidato ou None.
    """
    candidatos = carregar_db(DB_CANDIDATOS, Candidato)
    for cand in candidatos:
        if str(cand.numero) == str(numero):
            return cand
    return None

def computar_voto_candidato(numero_digitado):
    """
    Lê o banco de candidatos, incrementa o voto e salva o arquivo.
    """
    candidatos = carregar_db(DB_CANDIDATOS, Candidato)
    encontrado = False

    for cand in candidatos:
        if str(cand.numero) == str(numero_digitado):
            cand.votos += 1  # Incrementa o contador
            encontrado = True
            break
    
    if encontrado:
        # Salva a lista atualizada no arquivo
        dados_atualizados = [c.to_dict() for c in candidatos]
        try:
            with open(DB_CANDIDATOS, "w", encoding="utf-8") as f:
                json.dump(dados_atualizados, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Erro de sistema ao salvar voto: {e}")
            return False
            
    return False

def votar():
    print("\n--- SISTEMA DE VOTAÇÃO ---")
    
    # ==================================================
    # ETAPA 1: IDENTIFICAÇÃO E VERIFICAÇÃO DO ELEITOR
    # ==================================================
    cpf_digitado = input("Digite seu CPF: ").strip()
    
    lista_eleitores = carregar_db(DB_ELEITORES, Eleitor)
    eleitor_atual = None
    
    # Busca o eleitor
    for e in lista_eleitores:
        if e.cpf == cpf_digitado:
            eleitor_atual = e
            break
            
    # Validações de Login
    if eleitor_atual is None:
        print("Erro: CPF não encontrado no cadastro.")
        return

    # TRAVA DE SEGURANÇA: Verifica se já votou
    if eleitor_atual.ja_votou:
        print(f"ALERTA: O eleitor {eleitor_atual.nome} JÁ VOTOU nesta eleição!")
        print("Acesso negado para votar novamente.")
        return

    print(f"Login realizado com sucesso. Bem-vindo(a), {eleitor_atual.nome}.")

    # ==================================================
    # ETAPA 2: ESCOLHA DO CANDIDATO
    # ==================================================
    numero_digitado = ""
    
    while True:
        numero_digitado = input("\nDigite o número do candidato (ou 'S' para sair): ").strip()
        
        if numero_digitado.lower() == 's':
            print("Votação cancelada pelo usuário.")
            return

        # Verifica quem é o candidato antes de computar
        candidato_obj = buscar_candidato_info(numero_digitado)
        
        if candidato_obj:
            print(f"--- CONFIRMAÇÃO ---")
            print(f"Candidato: {candidato_obj.nome}")
            print(f"Partido:   {candidato_obj.partido}")
            print(f"Cargo:     {candidato_obj.cargo}")
            
            confirma = input("Confirma o voto? (S/N): ").strip().upper()
            if confirma == 'S':
                break # Sai do loop para efetivar o voto
            else:
                print("Voto cancelado. Digite o número novamente.")
        else:
            print("Numero invalido ou candidato inexistente.")

    # ==================================================
    # ETAPA 3: EFETIVAÇÃO E PERSISTÊNCIA
    # ==================================================
    
    # 1. Tenta salvar o voto no arquivo de candidatos
    sucesso_voto = computar_voto_candidato(numero_digitado)
    
    if sucesso_voto:
        # 2. Se o voto foi salvo, marca o eleitor como "já votou"
        eleitor_atual.ja_votou = True
        
        # 3. Salva a atualização no arquivo de eleitores
        dados_eleitores_atualizados = [e.to_dict() for e in lista_eleitores]
        
        try:
            with open(DB_ELEITORES, "w", encoding="utf-8") as f:
                json.dump(dados_eleitores_atualizados, f, ensure_ascii=False, indent=4)
            print("\nSUCESSO: Voto computado e eleitor atualizado.")
            print("Obrigado por votar!")
        except Exception as e:
            # Caso raríssimo onde salvou o voto mas falhou ao bloquear o eleitor
            print(f"Erro crítico ao atualizar status do eleitor: {e}")
    else:
        print("Erro: Não foi possível registrar o voto no banco de dados.")