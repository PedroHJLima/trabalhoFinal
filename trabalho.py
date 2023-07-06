from profissional import Profissional
from visitante import Visitante
from datetime import *
import json
import os
  

l_profissionais = []
l_visitantes = []
dict_visitas = {}
dicVisitantes = {}

############# OPÇÃO 1 ############

def CriaProfissional():
    """Recebe nome, profissão e sala e coloca o profissional na lista"""
    profissional = Profissional()

    nome = input("Qual o nome desse profissional?").capitalize()
    profissao = input("Qual sua profissão?")
    sala = input("Em qual sala ele trabalha?")

    # Verificar se o nome já existe na lista de profissionais
    for profissional in l_profissionais:
        if profissional.getDados()[0] == nome:
            input("Já existe um profissional com esse nome.\nEnter pra continuar")
            return

    profissional.setDados(nome, profissao, sala)

    l_profissionais.append(profissional)


############# OPÇÃO 2 ############

def criaVisitante():
    """Recebe nome e documento e atribui visitante na lista"""
    visitante = Visitante()

    nome = input("Qual o nome desse visitante?").capitalize()
    documento = input("Qual seu RG?")

    for visitante in l_visitantes:
        if visitante.getDados()[0] == nome:
            input("Já existe um visitante com esse nome.\nEnter pra continuar")
            return

    visitante.setDados(nome,documento)

    l_visitantes.append(visitante)


############# OPÇÃO 3 ############

def printOBJ(obj):
    for objeto in obj:
        print(objeto.getDados())

def buscaProfissional():
    lBusca = []
    dado = input("Você deseja acessar pelo nome ou pela profissão?\n1-Nome\n2-Profissão\Escolha: ")
    if dado == "1":
        #Buscar todos os profissionais com esse nome
        nome = input("Qual o nome desse profissional?").capitalize()
        for obj in l_profissionais:
            if obj.getDados()[0] == nome:
                lBusca.append(obj)
    
    elif dado == "2":
        #Buscar todos os profissionais dessa área
        profissao = input("Qual profissão você busca?")
        for obj in l_profissionais:
            if obj.getDados()[1] == profissao:
                lBusca.append(obj)

    else:
        input("Opção inexistente, Enter para continuar")

    return lBusca

############# OPÇÃO 4 ############

def testaVisitante():
    visitante = input("Qual o nome do visitante? ").capitalize()


    for obj in l_visitantes:
        if obj.getDados()[0] == visitante:
            return obj

def testaProfissional():
    profissional = input("Qual o nome do profissional?").capitalize()

    try:
        for obj in l_profissionais:
            if obj.getDados()[0] == profissional:
                return obj
    
    except:
        input("Profissional inexistente, enter:")

def registraVisita():
    """Pega visitante, profissional e horário do computador pra registrar uma visita
    em um dicionario de dados usando o nome do visitante como chave"""
    
    visitante = testaVisitante()
    profissional = testaProfissional()

    chave = visitante.getDados()[0]

    if chave in dict_visitas.keys():
        #Já existe uma visita nesse nome
        dict_visitas[chave].append([profissional.getDados()[0], datetime.now().strftime("%d/%m/%Y %H:%M"), profissional.getDados()[2]])
    else:
        #Nenhuma visita nesse nome
        dict_visitas[chave] = [profissional.getDados()[0], datetime.now().strftime("%d/%m/%Y %H:%M"), profissional.getDados()[2]]

############# OPÇÃO 5 ############

def visitasProfissional(dicionario, nome):
    dictVisitas = {}
    for chave, valor_atual in dicionario.items():
        if valor_atual[0] == nome:
            if valor_atual[0] in dictVisitas:
                # A chave já existe, atualizar o valor
                dictVisitas[valor_atual[0]].append((chave, valor_atual[1], valor_atual[2]))
            else:
                # A chave não existe, adicionar uma nova entrada
                dictVisitas[valor_atual[0]] = [chave, valor_atual[1], valor_atual[2]]
    return dictVisitas if dictVisitas else print("Profissional sem visitas registradas")

############# OPÇÃO 6 ############

def arquivaVisita():
    visitante = testaVisitante()

    try:
        chave = visitante.getDados()[1]
        nome = visitante.getDados()[0]
    except:
        input("Visitante inexistente")

        for chave in dict_visitas.keys():
            print(dict_visitas[nome][0], dict_visitas[nome][1], dict_visitas[nome][2])
            if chave in dicVisitantes.keys():
                #Já existe uma visita nesse nome
                dicVisitantes[chave].append([dict_visitas[nome][0], dict_visitas[nome][1], dict_visitas[nome][2]])
            else:
                #Nenhuma visita nesse nome
                dicVisitantes[chave] = [dict_visitas[nome][0], dict_visitas[nome][1], dict_visitas[nome][2]]


def salvarDadosEmJSON(dados, nome_arquivo):
    lista_dicionarios = []
    chaves_unicas = set()

    for chave, valores in dados.items():
        if chave not in chaves_unicas:
            chaves_unicas.add(chave)
            lista_dicionarios.append({
                chave: [
                    [valores[0], valores[1], valores[2]]
                ]
            })
        else:
            for dic in lista_dicionarios:
                if chave in dic:
                    dic[chave].append(valores[0], valores[1], valores[2])
                    break

    print(lista_dicionarios)
        
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista_dicionarios, arquivo)
        print(f"Dados salvos em '{nome_arquivo}' com sucesso.")



############# OPÇÃO 7 ############

def salvarObjetos(lista_objetos, nome_arquivo):
    """Salva os objetos em arquivo txt em formato json, ignorando caso já exista alguem com nome igual na lista para impedir duplicidade durante uso"""
    lista_tuplas = []
    for objeto in lista_objetos:
        tupla = objeto.getDados()
        lista_tuplas.append(tupla)

    if os.path.exists(nome_arquivo):
        print(f"O arquivo '{nome_arquivo}' já existe. Modificando o arquivo existente.")
        # Carregar o conteúdo existente do arquivo
        with open(nome_arquivo, 'r') as arquivo:
            conteudo_existente = json.load(arquivo)

        # Verificar se cada objeto já está presente na lista
        for tupla in lista_tuplas:
            nome_objeto = tupla[0]
            existe_no_arquivo = False

            for item in conteudo_existente:
                if item[0] == nome_objeto:
                    print(f"O objeto com o nome '{nome_objeto}' já existe no arquivo. Pulando a adição.")
                    existe_no_arquivo = True
                    break

            if not existe_no_arquivo:
                conteudo_existente.append(tupla)

        # Salvar o conteúdo modificado no arquivo
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(conteudo_existente, arquivo)
            print(f"Arquivo '{nome_arquivo}' modificado e salvo com sucesso.")
    else:
        # Salvar a lista de tuplas em um novo arquivo JSON
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(lista_tuplas, arquivo)
            print(f"Arquivo '{nome_arquivo}' criado e salvo com sucesso.")



############# OPÇÃO 8 ############

def arquivoInexistente():
    input("Arquivo(s) inexistente(s). Enter para continuar")

def deleta():
    arquivo = input("Qual arquivo você deseja deletar?\n1-Deletar lista de profissionais\n\
2- Deletar lista de visitantes\n3-Ambos\nEscolha: ")
    if arquivo =="1":
        if os.path.exists("profissionais.txt"):
            #Quero deletar todos os profissionais
            os.remove("profissionais.txt") 
            input("Lista de profissionais excluída. Enter para continuar!") 
        else:
            input(arquivoInexistente())
    
    elif arquivo == "2":
        if os.path.exists("visitantes.txt"):
            #Quero deletar todos os visitantes
            os.remove("visitantes.txt")
        else:
            input(arquivoInexistente())
    
    elif arquivo == "3":
        if os.path.exists("visitantes.txt") and os.path.exists("profissionais.txt"):
            #Remove os dois
            os.remove("visitantes.txt")
            os.remove("profissionais.txt")
        else:
            input(arquivoInexistente())

    else:
        input("Opção invalida")


############# MAIN ############



def iniciar():
    if os.path.exists('profissionais.txt'):
        #Arquivo já existe, carregar e popular dicionario
        resgataObjetos("profissionais.txt", Profissional, Profissional.setDados,l_profissionais)
        print(l_profissionais)
    if os.path.exists('visitantes.txt'):
        #Arquivo de visitas existente
        resgataObjetos("visitantes.txt", Visitante, Visitante.setDados,l_visitantes)
        print(l_visitantes)

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
7- Salvar atualizações nos arquivos\n\
8- Limpar arquivos\n\
Escolha:")

def resgataObjetos(nome_arquivo, classe_objeto, metodo_setDados,lista_objetos):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = json.load(arquivo)
    for item in conteudo:
        objeto = classe_objeto()
        metodo_setDados(objeto, *item)
        lista_objetos.append(objeto)

#-----Início-----
#Antes de começar o código, tem que verificar se já existem profissionais e visitantes cadastrados
iniciar()
    

while True:
    print(dict_visitas)
    escolha = menu()

    if escolha == "1":
        #Cadastrar Profissional
        CriaProfissional()

    elif escolha == "2":
        #Cadastrar visitante
        criaVisitante()

    elif escolha == "3":
        #Buscar profissional pelo nome ou sala e devolver nome profissão e sala
        printOBJ(buscaProfissional())

    elif escolha == "4":
        #Registrar uma visita agora
        registraVisita()

    elif escolha == "5":
        #Quero ver quais visitas tal profissional recebeu. Devolvendo nome do visitante e a data da visita
        profissional = input("Qual nome do profissional?").capitalize()

        busca = visitasProfissional(dict_visitas,profissional)
        print(busca)

    elif escolha == "6":
        #gerar um arquivo JSON com o registro do dia
        arquivaVisita()
        salvarDadosEmJSON(dict_visitas,'visitasRealizadas')

    elif escolha == "7":
        #Salva na lista existente os profissionais adicionados durante o uso
        salvarObjetos(l_profissionais,'profissionais.txt')
        salvarObjetos(l_visitantes,'visitantes.txt')
    
    elif escolha == "8":
        #Limpar os arquivos e as listas
        deleta()
        l_profissionais.clear()
        l_visitantes.clear()
        