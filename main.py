# main.py
from models.candidato import Candidato
from controller.controller_candidato import cadastrar_candidato
from utils.menu import menu

def main():
    while True:
        if menu():
            break

if __name__ == "__main__":
    main()
