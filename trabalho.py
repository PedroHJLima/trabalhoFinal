from profissional import Profissional
from visitante import Visitante
  

class Visita:
    print()

l_profissionais = []
l_visitantes = []

def CriaProfissional():
    """Recebe nome, profissão e sala e coloca o profissional na lista"""
    profissional = Profissional()

    nome = input("Qual o nome desse profissional?").upper()
    profissao = input("Qual sua profissão?")
    sala = input("Em qual sala ele trabalha?")

    profissional.setDados(nome,profissao,sala)

    l_profissionais.append(profissional)

def criaVisitante():
    """Recebe nome e documento e atribui visitante na lista"""
    profissional = Profissional()

    nome = input("Qual o nome desse profissional?").upper()
    profissao = input("Qual sua profissão?")
    sala = input("Em qual sala ele trabalha?")

    profissional.setDados(nome,profissao,sala)

    l_profissionais.append(profissional)

def buscaProfissional():
    dado = input("Você deseja acessar pelo nome ou pela profissão?")
    if dado == "nome":
        #Buscar pelo nome
        nome = input("Qual o nome desse profissional?").upper
        for obj in l_profissionais:
            if obj.getDados()[0] == nome:
                print(obj.getDados())

    elif dado == "profissão":
        #Buscar pela profissão
        profissao = input("Qual profissão você busca?").upper
        for obj in l_profissionais:
            if obj.getDados()[1] == profissao:
                print(obj.getDados())

    else:
        print("Opção inexistente")


#-----Início-----
while True:
    escolha = input(f"======================\n\
MENU\n\
======================\n\
1- Cadastrar Profissional\n\
2- Cadastrar Visitante\n\
3- Localizar Profissional\n\
4- Registrar Visita\n\
5- Relatório de Conferência\n\
6- Gerar arquivo de Registros do dia\n\
7- Ler arquivos profissionais / visitantes\n\
Escolha:")

    if escolha == "1":
        #Cadastrar Profissional
        CriaProfissional()

    elif escolha == "2":
        #Cadastrar visitante
        criaVisitante()

    elif escolha == "3":
        #Buscar profissional pelo nome ou sala e devolver nome profissão e sala
        buscaProfissional()

    elif escolha == "4":
        #Registrar uma visita agora
        print()
        