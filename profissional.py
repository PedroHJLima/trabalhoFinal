class Profissional:
    def __init__(self):
        self.__dados = {
            "Nome": "nome",
            "Profissao": "profissao",
            "Sala": "sala"
        }

    def setDados(self,nome,profissao,sala):
        """Seta os dados da pesquisa"""
        self.__dados[0] = nome
        self.__dados[1] = profissao
        self.__dados[2] = sala

    def getDados(self):
        """Seta os dados da pesquisa"""
        nome = self.__dados[0]
        profissao = self.__dados[1]
        sala = self.__dados[2]

        return nome, profissao, sala

    def __repr__(self):
        return f"Nome: {self.__dados[0]}\n Profissão: {self.__dados[1]}\nSala: {self.__dados[2]}"