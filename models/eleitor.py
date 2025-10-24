class Eleitor:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf
        }
