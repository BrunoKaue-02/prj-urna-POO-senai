class Partido:
    def __init__(self, nome_partido, sigla, numero_partido):
        self.nome_partido = nome_partido
        self.sigla = sigla
        self.numero_partido = numero_partido

    def to_dict(self):
        return {
            "nome_partido": self.nome_partido,
            "sigla": self.sigla,
            "numero_partido": self.numero_partido
        }
