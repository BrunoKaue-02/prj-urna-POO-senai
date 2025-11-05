import os
from dotenv import load_dotenv
from utils.voto_utils import apagar_db_json

load_dotenv()

db_eleitores = os.getenv("JSON_PATH_VOTOS")

def reiniciar_votacao():
    escolha = input("Deseja reiniciar a votação? (s/n): ")
    if escolha.lower() == "s":
        apagar_db_json(db_eleitores)
        print("Votação reiniciada.")
    else:
        print("Votação não reiniciada.")