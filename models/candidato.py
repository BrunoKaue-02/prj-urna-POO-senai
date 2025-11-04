from models.eleitor import Eleitor

class Candidato(Eleitor):
    def __init__(self, nome, idade, cpf, partido, numero, cargo):
        super().__init__(nome, idade, cpf)
        self.partido = partido
        self.numero = numero
        self.cargo = cargo

    def to_dict(self):
        dados = super().to_dict()  # pega os dados da classe Pessoa
        dados.update({
            "partido": self.partido,
            "numero": self.numero,
            "cargo" : self.cargo
        })
        return dados

