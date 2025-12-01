from controller.controller_candidato import cadastrar_candidato, apagar_candidato, listar_candidatos
from controller.controller_eleitor import cadastrar_eleitor, listar_eleitores, apagar_eleitor
from controller.controller_partido import cadastrar_partido, listar_partidos, apagar_partido
from controller.controller_voto import votar
from controller.controller_resultados import finalizar_votacao 
import os
from dotenv import load_dotenv

load_dotenv()


senha_admin = os.getenv("SENHA_ADMIN",)

def menu():
    print("\n=== URNA ELETRÔNICA ===")
    print("1. Cadastro")
    print("2. Votar")
    print("3. Finalizar votação")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            menu_cadastro()
        case "2":
            votar()
        case "3":
            senha = input("Digite a senha de administrador para finalizar a votação: ")
            if senha != senha_admin:
                print("Senha incorreta. Acesso negado.")
            elif senha == senha_admin:
                finalizar_votacao()
            else:
                print("Senha incorreta. Acesso negado.")
        case "4":
            print("Saindo do programa...")
            return True
        case _:
            print("Opção inválida. Tente novamente.")


def menu_cadastro():
    print("\n--- Menu Cadastro ---")  
    print("1. Cadastro candidato")
    print("2. Cadastro eleitor")
    print("3. Cadastro partido")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            menu_candidato()
        case "2":
            menu_eleitor()
        case "3":
            cadastro_partido()
        case "4":
            menu()
        case _:
            print("Opção inválida. Tente novamente.")   

def menu_eleitor():
    print("\n--- Menu Eleitor ---")
    print("1. Cadastrar eleitor")
    print("2. Listar eleitores")
    print("3. Apagar eleitor")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            cadastrar_eleitor()
        case "2":
            listar_eleitores()
        case "3":
            apagar_eleitor()
        case "4":
            menu_cadastro()
        case _:
            print("Opção inválida. Tente novamente.")


def menu_candidato():
    print("\n--- Menu Candidato ---")
    print("1. Cadastrar candidato")
    print("2. Listar candidatos")
    print("3. Apagar candidato")
    print("4. Sair\n")

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            cadastrar_candidato()
        case "2":
            listar_candidatos()
        case "3":
            apagar_candidato()
        case "4":
            menu_cadastro()
        case _:
            print("Opção inválida. Tente novamente.")

def cadastro_partido():
    print("\n--- Menu Partido ---") 
    print("1. Cadastrar partido")
    print("2. Listar partidos")
    print("3. Apagar partido")
    print("4. Sair\n")  

    escolha = input("Escolha uma opção: ")

    match escolha:
        case "1":
            cadastrar_partido()
        case "2":
            listar_partidos()
        case "3":
            apagar_partido()
        case "4":
            menu_cadastro()
        case _:
            print("Opção inválida. Tente novamente.")   

