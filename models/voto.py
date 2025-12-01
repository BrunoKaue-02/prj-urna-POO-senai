class ContagemVoto:
    # Note que os parametros batem com o JSON que você pediu
    def __init__(self, candidato, numero_do_candidato, quantidade_de_votos=0):
        self.candidato = candidato
        self.numero_do_candidato = numero_do_candidato
        self.quantidade_de_votos = quantidade_de_votos

    def to_dict(self):
        return {
            "candidato": self.candidato,
            "numero_do_candidato": self.numero_do_candidato,
            "quantidade_de_votos": self.quantidade_de_votos
        }