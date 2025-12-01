class Eleitor:
    def __init__(self, nome, idade, cpf,ja_votou=False):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.ja_votou = ja_votou

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "cpf": self.cpf,
            "ja_votou": self.ja_votou
        }
