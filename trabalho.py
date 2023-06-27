from profissional import Profissional
from visitante import Visitante
from datetime import *
import json
import os
  

l_profissionais = []
l_visitantes = []
dict_visitas = {}

def CriaProfissional():
    """Recebe nome, profissão e sala e coloca o profissional na lista"""
    profissional = Profissional()

    nome = input("Qual o nome desse profissional?").capitalize()
    profissao = input("Qual sua profissão?")
    sala = input("Em qual sala ele trabalha?")

    profissional.setDados(nome,profissao,sala)

    l_profissionais.append(profissional)

def criaVisitante():
    """Recebe nome e documento e atribui visitante na lista"""
    visitante = Visitante()

    nome = input("Qual o nome desse visitante?").capitalize()
    documento = input("Qual seu RG?")

    visitante.setDados(nome,documento)

    l_visitantes.append(visitante)

def buscaProfissional():
    dado = input("Você deseja acessar pelo nome ou pela profissão?")
    if dado == "nome":
        #Buscar pelo nome
        nome = input("Qual o nome desse profissional?").capitalize()
        for obj in l_profissionais:
            print(obj)
            if obj.getDados()[0] == nome:
                print(obj)
            else:
                print(f"não existe um profissional com o nome {nome}")

    elif dado == "profissão":
        #Buscar pela profissão
        profissao = input("Qual profissão você busca?")
        for obj in l_profissionais:
            if obj.getDados()[1] == profissao:
                print(obj.getDados())

    else:
        print("Opção inexistente")

def testaVisitante():
    visitante = input("Qual o nome do visitante? ").capitalize()

    for obj in l_visitantes:
        if obj.getDados()[0] == visitante:
            return obj

def testaProfissional():
    profissional = input("Qual o nome do profissional?").capitalize()

    for obj in l_profissionais:
        if obj.getDados()[0] == profissional:
            return obj
    
    else:
        print("profissional não existe")

def registraVisita():
    """Pega visitante, profissional e horário do computador pra registrar uma visita
    em um dicionario de dados usando o nome do visitante como chave"""
    
    visitante = testaVisitante()
    profissional = testaProfissional()

    print(visitante)
    chave = visitante.getDados()[0]
    #valor = (profissional.getDados()[0], datetime.now().strftime("%d/%m/%Y %H:%M"), profissional.getDados()[2])
    dict_visitas[chave] = [profissional.getDados()[0], datetime.now().strftime("%d/%m/%Y %H:%M"), profissional.getDados()[2]]

def visitasProfissional(dicionario, nome):
    dictVisitas = {}
    for chave, valor_atual in dicionario.items():
        if valor_atual[0] == nome:
            if valor_atual[0] in dictVisitas:
                # A chave já existe, atualizar o valor
                dictVisitas[valor_atual[0]].append((chave, valor_atual[1], valor_atual[2]))
            else:
                # A chave não existe, adicionar uma nova entrada
                dictVisitas[valor_atual[0]] = [(chave, valor_atual[1], valor_atual[2])]
    return dictVisitas if dictVisitas else None

def salvarProfissionais(lista_objetos, nome_arquivo):
    # Converter a lista de objetos em uma lista de dicionários
    lista_dicionarios = []
    for objeto in lista_objetos:
        dicionario = {
            'nome': objeto.getDados()[0],
            'profissao': objeto.getDados()[1],
            'sala': objeto.getDados()[2]
        }
        lista_dicionarios.append(dicionario)       

    if os.path.exists(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' já existe. Modificando o arquivo existente.")
        # Abrir o arquivo em modo de leitura e escrita
        with open(nome_arquivo, 'r+') as arquivo:
            # Carregar o conteúdo existente do arquivo
            conteudo_existente = json.load(arquivo)

            # Modificar o conteúdo existente com a nova lista de dicionários
            conteudo_existente.extend(lista_dicionarios)

            # Posicionar o cursor no início do arquivo
            arquivo.seek(0)

            # Salvar o conteúdo modificado no arquivo
            json.dump(conteudo_existente, arquivo)
    else:
        # Salvar a lista de dicionários em um novo arquivo JSON
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(lista_dicionarios, arquivo)
            print(f"Arquivo '{nome_arquivo}' criado e salvo com sucesso.")

def resgatar_objetos_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = json.load(arquivo)
    for item in conteudo:
        profissional = Profissional()
        profissional.setDados(item["nome"],item["profissao"],item["sala"])
        l_profissionais.append(profissional)

def menu():
    return input(f"======================\n\
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


#-----Início-----
while True:
    #Antes de começar o código, tem que verificar se já existem profissionais e visitantes cadastrados
    if os.path.exists('profissionais'):
        #Arquivo já existe, carregar e popular dicionario
        chaves = resgatar_objetos_do_arquivo('profissionais')

    print(l_profissionais)

    escolha = menu()

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
        registraVisita()

    elif escolha == "5":
        #Quero ver quais visitas tal profissional recebeu. Devolvendo nome do visitante e a data da visita
        profissional = input("Qual nome do profissional?").capitalize()

        ########################
        #CUIDADO -- COM ISSO, SÓ MOSTRA A PRIMEIRA VISITA DESSE PROFISSIONAL.
        #ALTERAR PRA MOSTRAR TODAS
        ####################
        busca = visitasProfissional(dict_visitas,profissional)
        print(busca)

    elif escolha == "6":
        #gerar um arquivo com o registro do dia
        print()

    elif escolha == "7":
        #Salvar a lista atual
        salvarProfissionais(l_profissionais,'profissionais')
    
        