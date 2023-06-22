class Visitante:
    def __init__(self):
        self.__dados = {
            "Nome": "nome",
            "Documento": "documento",
        }

    def setDados(self,nome,documento):
        """Seta os dados da pesquisa"""
        self.__dados[0] = nome
        self.__dados[1] = documento

    def getDados(self):
        """Seta os dados da pesquisa"""
        nome = self.__dados[0]
        documento = self.__dados[1]

        return nome, documento

    def __repr__(self):
        return f"Nome: {self.__dados[0]}\n Documento: {self.__dados[1]}"
