from models.eleitor import Eleitor

class Candidato(Eleitor):
    def __init__(self, nome, idade, cpf, partido, numero, cargo, votos=0, ja_votou=False):
        # garante que o campo 'ja_votou' (herdado de Eleitor) seja aceito quando
        # construímos a partir de um dict carregado do JSON
        super().__init__(nome, idade, cpf, ja_votou)
        self.partido = partido
        self.numero = numero
        self.cargo = cargo
        self.votos = votos # Novo campo contador

    def to_dict(self):
        dados = super().to_dict()
        dados.update({
            "partido": self.partido,
            "numero": self.numero,
            "cargo": self.cargo,
            "votos": self.votos
        })
        return dados